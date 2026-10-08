# -*- coding: utf-8 -*-
"""
Cliente STOMP mínimo sobre WebSocket nativo usando websocket-client.
Soporta: CONNECT, SUBSCRIBE, SEND, DISCONNECT.

Requiere: pip install websocket-client
"""

import json
import threading
import time
import uuid
from typing import Callable, Dict, Optional

from websocket import WebSocketApp


# ---------------------------
# Utilidades STOMP
# ---------------------------

def _build_frame(command: str, headers: Dict[str, str], body: Optional[str] = None) -> str:
    """
    Construye un frame STOMP:
    COMMAND\r\n
    key:value\r\n
    ...
    \r\n
    <body>\x00
    """
    # STOMP permite \n; muchos servidores aceptan \n o \r\n. Usamos \n.
    lines = [command]
    for k, v in headers.items():
        # Aseguramos string y evitamos \n en headers
        v = "" if v is None else str(v)
        v = v.replace("\n", " ")
        lines.append(f"{k}:{v}")
    # Línea en blanco que separa headers del cuerpo
    frame = "\n".join(lines) + "\n\n"
    if body is not None:
        frame += body
    # Terminador null char
    frame += "\x00"
    return frame


def _parse_frame(raw: str) -> Dict[str, str]:
    """
    Parsea un frame STOMP de texto y devuelve dict con:
    { 'command': str, 'headers': dict, 'body': str }
    """
    # Eliminamos posibles \r
    raw = raw.replace("\r", "")
    # Un frame STOMP termina en \x00. Si hay paquetes pegados, el WebSocketApp
    # suele entregarlos separados; si no, aquí podrías split por \x00 y procesar varios.
    if "\x00" in raw:
        raw = raw.split("\x00", 1)[0]

    # Separa encabezados de cuerpo
    head, sep, body = raw.partition("\n\n")
    header_lines = head.split("\n")
    command = header_lines[0].strip()
    headers = {}
    for line in header_lines[1:]:
        if not line.strip():
            continue
        k, _, v = line.partition(":")
        headers[k.strip()] = v.strip()
    return {"command": command, "headers": headers, "body": body}


# ---------------------------
# Cliente STOMP sobre WS
# ---------------------------

class StompWSClient:
    """
    Cliente STOMP simple que usa websocket-client (WebSocketApp) en un hilo.
    - connect_async(url, on_connected, on_message, on_error)
    - subscribe(destination)
    - send(destination, body, content_type="application/json")
    - disconnect()

    Callbacks:
      on_connected(): llamado cuando llega el frame CONNECTED
      on_message(frame): dict {'command','headers','body'} para MESSAGE/ERROR/etc.
      on_error(exc): errores de socket o del hilo
    """

    def __init__(self, host_header: str = "localhost", heartbeat_ms: int = 0):
        self._url: Optional[str] = None
        self._ws: Optional[WebSocketApp] = None
        self._thread: Optional[threading.Thread] = None
        self._connected = False
        self._session_id = None
        self._subscriptions = {}
        self._host_header = host_header
        self._heartbeat_ms = heartbeat_ms  # p.ej. 0 o 10000

        # Callbacks
        self._on_connected: Optional[Callable[[], None]] = None
        self._on_message: Optional[Callable[[Dict[str, str]], None]] = None
        self._on_error: Optional[Callable[[Exception], None]] = None

        # lock envío
        self._send_lock = threading.Lock()

    # ------------- WebSocketApp Callbacks -------------

    def _ws_on_open(self, ws):
        # Enviar CONNECT STOMP
        headers = {
            "accept-version": "1.2",
            "host": self._host_header,
            "heart-beat": f"{self._heartbeat_ms},{self._heartbeat_ms}" if self._heartbeat_ms else "0,0"
        }
        frame = _build_frame("CONNECT", headers)
        with self._send_lock:
            ws.send(frame)

    def _ws_on_message(self, ws, message):
        try:
            frame = _parse_frame(message)
        except Exception as e:
            if self._on_error:
                self._on_error(e)
            return

        cmd = frame.get("command", "")
        if cmd == "CONNECTED":
            self._connected = True
            self._session_id = frame.get("headers", {}).get("session")
            if self._on_connected:
                self._on_connected()
            return

        # Reenvía MESSAGE, RECEIPT, ERROR, etc. al callback
        if self._on_message:
            self._on_message(frame)

    def _ws_on_error(self, ws, error):
        if self._on_error:
            # Aseguramos Exception
            exc = error if isinstance(error, Exception) else Exception(str(error))
            self._on_error(exc)

    def _ws_on_close(self, ws, close_status_code, close_msg):
        self._connected = False

    # ------------- API Pública -------------

    def connect_async(
        self,
        url: str,
        on_connected: Optional[Callable[[], None]] = None,
        on_message: Optional[Callable[[Dict[str, str]], None]] = None,
        on_error: Optional[Callable[[Exception], None]] = None,
        sslopt: Optional[dict] = None,
    ):
        """
        Conecta en un hilo (no bloqueante).
        """
        self._url = url
        self._on_connected = on_connected
        self._on_message = on_message
        self._on_error = on_error

        self._ws = WebSocketApp(
            url,
            on_open=self._ws_on_open,
            on_message=self._ws_on_message,
            on_error=self._ws_on_error,
            on_close=self._ws_on_close,
        )

        def _run():
            # Nota: run_forever bloquea hasta cerrar; lo hacemos en hilo propio
            # sslopt solo necesario si usas wss:// (certificados, etc.)
            try:
                if sslopt is not None:
                    self._ws.run_forever(sslopt=sslopt)
                else:
                    self._ws.run_forever()
            except Exception as e:
                if self._on_error:
                    self._on_error(e)

        self._thread = threading.Thread(target=_run, daemon=True)
        self._thread.start()

    def subscribe(self, destination: str, ack: str = "auto") -> str:
        """
        Envía SUBSCRIBE; devuelve el id de la suscripción.
        """
        if not self._ws or not self._connected:
            raise RuntimeError("WebSocket/STOMP no conectado aún.")

        sub_id = str(uuid.uuid4())
        headers = {
            "id": sub_id,
            "destination": destination,
            "ack": ack,
        }
        frame = _build_frame("SUBSCRIBE", headers)
        with self._send_lock:
            self._ws.send(frame)

        self._subscriptions[sub_id] = destination
        return sub_id

    def send(self, destination: str, body: str, content_type: str = "application/json"):
        """
        Envía SEND a un destino STOMP (generalmente /app/* para app, /topic/* o /queue/* para broker).
        """
        if not self._ws or not self._connected:
            raise RuntimeError("WebSocket/STOMP no conectado aún.")

        headers = {
            "destination": destination,
            "content-type": content_type,
            "content-length": str(len(body.encode("utf-8"))),
        }
        frame = _build_frame("SEND", headers, body)
        with self._send_lock:
            self._ws.send(frame)

    def disconnect(self, receipt: bool = False):
        """
        Envía DISCONNECT y cierra el socket.
        """
        if self._ws:
            headers = {}
            if receipt:
                headers["receipt"] = str(uuid.uuid4())
            frame = _build_frame("DISCONNECT", headers)
            try:
                with self._send_lock:
                    self._ws.send(frame)
            except Exception:
                pass
            # Pequeña espera para que se envíe el frame
            time.sleep(0.05)
            try:
                self._ws.close()
            except Exception:
                pass

        self._connected = False
        self._ws = None
        self._thread = None
        self._subscriptions.clear()

    def get_session_id(self) -> Optional[str]:
        """Devuelve el session-id obtenido del CONNECTED (si disponible)."""
        return self._session_id

    def is_connected(self) -> bool:
        return bool(self._connected)