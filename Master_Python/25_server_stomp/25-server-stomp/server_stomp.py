#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Servidor STOMP 1.2 mínimo sobre WebSocket nativo (sin SockJS).
- Escucha en 0.0.0.0:8080 y acepta cualquier path.
- Soporta CONNECT, SUBSCRIBE, SEND, DISCONNECT.
- StompBroker mantiene en memoria:
    - history: list[dict] de mensajes (solo guarda si type == "MESSAGE").
    - suscripciones por sesión.
- Solo recibe SEND a /app/message con JSON {username, text, date, type}
- Publica a suscriptores de /chat/message (no eco al emisor).
"""

import asyncio
import json
import logging
import secrets
from datetime import datetime, timezone
from itertools import count
from typing import Dict, Any, Tuple, List
import random

import websockets
from websockets import ServerConnection
from models.message import Message as DbMessage
from repositories.message_repository_impl import MessageRepositoryImpl

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


# ----------------------------
# Utils STOMP
# ----------------------------

NULL = "\x00"


def parse_frames(data: Any) -> List[Tuple[str, Dict[str, str], str]]:
    """
    Parsea 1..N frames STOMP 1.2 contenidos en un único mensaje WS (texto).
    Formato:
      COMMAND\n
      header1:value1\n
      header2:value2\n
      ...
      \n
      body\x00
    Puede venir más de un frame concatenado por \x00.
    """
    if isinstance(data, bytes):
        data = data.decode("utf-8", "replace")

    frames: List[Tuple[str, Dict[str, str], str]] = []
    # Un mensaje WS puede traer varios frames separados por NULL
    for chunk in data.split(NULL):
        if not chunk.strip():
            continue
        # STOMP permite un LF inicial opcional
        if chunk.startswith("\n"):
            chunk = chunk[1:]

        # Separar cabeceras y cuerpo por el primer doble LF
        if "\n\n" in chunk:
            header_section, body = chunk.split("\n\n", 1)
        else:
            header_section, body = chunk, ""

        lines = header_section.split("\n")
        command = lines[0].strip()
        headers: Dict[str, str] = {}
        for line in lines[1:]:
            if not line:
                continue
            if ":" in line:
                k, v = line.split(":", 1)
                headers[k.strip()] = v.strip()

        frames.append((command, headers, body))
    return frames


def build_frame(command: str, headers: Dict[str, str] | None = None, body: str = "") -> str:
    """
    Construye un frame STOMP (sin content-length).
    """
    headers = headers or {}
    lines = [command]
    for k, v in headers.items():
        lines.append(f"{k}:{v}")
    payload = "\n".join(lines) + "\n\n" + (body or "")
    return payload + NULL


# ----------------------------
# Broker
# ----------------------------

class Session:
    def __init__(self, ws: ServerConnection, session_id: str):
        self.ws = ws
        self.id = session_id
        # map subscription-id -> destination
        self.subscriptions: Dict[str, str] = {}


class StompBroker:
    """
    Broker mínimo en memoria.
    - history: list[dict]
    - sesiones y suscripciones
    """

    def __init__(self):
        # self.history: List[Dict[str, Any]] = []
        self.sessions: Dict[str, Session] = {}
        self._message_id_gen = count(1)
        # Paleta de 10 colores compatibles con Tkinter
        self.palette: List[str] = ["red", "orange", "gold", "green", "teal",
                                   "blue", "purple", "magenta", "brown", "gray"]
        # Mapa username -> color asignado
        self.user_colors: Dict[str, str] = {}
        # Repo de mensajes (MySQL/SQLAlchemy)
        self.repo = MessageRepositoryImpl()

    def on_connect(self, ws: ServerConnection) -> str:
        session_id = secrets.token_hex(8)
        self.sessions[session_id] = Session(ws, session_id)
        logging.info("CONNECT session_id=%s", session_id)
        return session_id

    def on_disconnect(self, session_id: str) -> None:
        sess = self.sessions.pop(session_id, None)
        if sess:
            logging.info("DISCONNECT session_id=%s (subs=%d)", session_id, len(sess.subscriptions))

    async def handle_connect(self, session: Session, headers: Dict[str, str]) -> None:
        """
        Responde CONNECTED 1.2. No negociamos heart-beats (0,0).
        """
        version = headers.get("accept-version", "1.2")
        # Forzamos 1.2 (mínimo requerido).
        resp = build_frame(
            "CONNECTED",
            {
                "version": "1.2",
                "heart-beat": "0,0",
                # 'server' es opcional, útil para debug:
                "server": "minimal-stomp-ws/0.1",
                "session": session.id,  # para que el cliente conozca su sessionId
            },
        )
        await session.ws.send(resp)

    async def handle_subscribe(self, session: Session, headers: Dict[str, str]) -> None:
        """
        Registra la suscripción. STOMP 1.2 requiere 'id' y 'destination'.
        No enviamos RECEIPT salvo que el cliente lo pida con 'receipt'.
        """
        dest = headers.get("destination")
        sub_id = headers.get("id")
        if not dest or not sub_id:
            # ERROR frame por cumplimiento básico
            err = build_frame(
                "ERROR",
                {"message": "SUBSCRIBE missing 'destination' or 'id'"},
                "SUBSCRIBE must include 'destination' and 'id'",
            )
            await session.ws.send(err)
            return

        session.subscriptions[sub_id] = dest
        logging.info("SUBSCRIBE session_id=%s id=%s dest=%s", session.id, sub_id, dest)

        receipt = headers.get("receipt")
        if receipt:
            await session.ws.send(build_frame("RECEIPT", {"receipt-id": receipt}))

    async def handle_send(self, session: Session, headers: Dict[str, str], body: str) -> None:
        """
        Acepta solo SEND a /app/message con body JSON {username, text, date, type}.
        Si type == 'MESSAGE' => guarda en history.
        Publica a suscriptores de /chat/message (no eco al emisor).
        """
        dest = headers.get("destination")
        if dest not in ("/app/message", "/app/history", "/app/writing"):
            logging.info("SEND ignorado (destination=%s)", dest)
            return

        try:
            payload = json.loads(body or "{}")
        except json.JSONDecodeError:
            err = build_frame("ERROR", {"message": "invalid JSON body"}, "Body must be valid JSON")
            await session.ws.send(err)
            return

        if dest == "/app/history":
            # Responder historial solo al cliente de esta sesión,
            # publicando en /chat/history/{sessionId}
            limit = payload.get("limit", 50)
            try:
                limit = int(limit)
            except Exception:
                limit = 50
            if limit <= 0:
                limit = 1
                # Cargar últimos N desde MySQL (solo MESSAGE), orden cronológico asc
            rows = self.repo.get_last_messages(limit=limit)
            items = [
                {
                    "username": r.username,
                    "text": r.text or "",
                    "date": (r.date or r.created_at).isoformat(timespec="seconds"),
                    "type": r.type,
                    "color": r.color,
                }
                for r in rows
            ]
            # items = self.history[-limit:]
            body_out = json.dumps(items, ensure_ascii=False)
            await self._send_to_session(
                session=session,
                destination=f"/chat/history/{session.id}",
                body=body_out,
            )

            receipt = headers.get("receipt")
            if receipt:
                await session.ws.send(build_frame("RECEIPT", {"receipt-id": receipt}))
            return

        # ------------------ WRITING ------------------
        if dest == "/app/writing":
            dictUsername = payload
            msg = json.dumps(dictUsername, ensure_ascii=False)
            await self._broadcast(
                destination="/chat/writing",
                body=msg,
                exclude_session_id=session.id,
            )
            receipt = headers.get("receipt")
            if receipt:
                await session.ws.send(build_frame("RECEIPT", {"receipt-id": receipt}))
            return

        # Validamos campos mínimos (suaves, es un demo)
        username = payload.get("username")
        text = payload.get("text")
        date = payload.get("date")
        msg_type = payload.get("type")

        if msg_type == "NEW_USER":
            # Asignar color si no viene, y recordar
            color = payload.get("color")
            if not color:
                color = self.user_colors.get(username) or random.choice(self.palette)
            self.user_colors[username] = color
            # Publicamos a TODOS (incluido el emisor) el aviso de nuevo usuario
            out = {
                "username": username,
                "text": f"{username} se ha conectado",
                "date": date or datetime.now().isoformat(timespec="seconds"),
                "type": "NEW_USER",
                "color": color,
            }
            await self._broadcast(
                destination="/chat/message",
                body=json.dumps(out, ensure_ascii=False),
                exclude_session_id=None,
            )
            receipt = headers.get("receipt")
            if receipt:
                await session.ws.send(build_frame("RECEIPT", {"receipt-id": receipt}))
            return

        if msg_type == "MESSAGE":
            # Enriquecer con color si lo conocemos y persistir en historial
            color = self.user_colors.get(username)

            # Guardar en MySQL
            try:
                dt = None
                try:
                    dt = datetime.fromisoformat(date) if date else None
                except Exception:
                    dt = None
                entity = DbMessage(
                    username=username or "Anon",
                    text=text or "",
                    date=dt or datetime.now(timezone.utc),
                    type="MESSAGE",
                    color=color,
                )
                self.repo.save(entity)
            except Exception as ex:
                logging.warning("No se pudo persistir mensaje en DB: %s", ex)

            # self.history.append({
            #     "username": username,
            #     "text": text,
            #     "date": date,
            #     "type": msg_type,
            #     "color": color,
            # })

        # Re-publicamos como MESSAGE a /chat/message (inyectando color)
        color = self.user_colors.get(username) or payload.get("color")
        enriched = dict(payload)
        if color:
            enriched["color"] = color
        message_id = next(self._message_id_gen)
        body_out = json.dumps(enriched, ensure_ascii=False)
        # Enviamos un frame MESSAGE por cada suscripción a /chat/message
        await self._broadcast(
            destination="/chat/message",
            body=body_out,
            exclude_session_id=session.id
        )

        receipt = headers.get("receipt")
        if receipt:
            await session.ws.send(build_frame("RECEIPT", {"receipt-id": receipt}))

    async def _broadcast(self, destination: str, body: str, exclude_session_id: str | None = None) -> None:
        for sess in list(self.sessions.values()):
            if exclude_session_id and sess.id == exclude_session_id:
                continue

            # Todas las suscripciones del session a ese destino
            sub_ids = [sid for sid, dest in sess.subscriptions.items() if dest == destination]
            if not sub_ids:
                continue

            for sid in sub_ids:
                msg_id = next(self._message_id_gen)
                frame = build_frame(
                    "MESSAGE",
                    {
                        "subscription": sid,
                        "message-id": str(msg_id),
                        "destination": destination,
                        "content-type": "application/json; charset=utf-8",
                    },
                    body,
                )
                try:
                    await sess.ws.send(frame)
                except Exception as exc:
                    logging.warning("Error enviando a session=%s: %s", sess.id, exc)

    async def _send_to_session(self, session: "Session", destination: str, body: str) -> None:
        """
        Envía un MESSAGE solo a las suscripciones del 'session' que coincidan con 'destination'.
        """
        sub_ids = [sid for sid, dest in session.subscriptions.items() if dest == destination]
        if not sub_ids:
            return
        for sid in sub_ids:
            msg_id = next(self._message_id_gen)
            frame = build_frame(
                "MESSAGE",
                {
                    "subscription": sid,
                    "message-id": str(msg_id),
                    "destination": destination,
                    "content-type": "application/json; charset=utf-8",
                },
                body,
            )
            try:
                await session.ws.send(frame)
            except Exception as exc:
                logging.warning("Error enviando historial a session=%s: %s", session.id, exc)


    async def handle_disconnect(self, session: Session, headers: Dict[str, str]) -> None:
        receipt = headers.get("receipt")
        if receipt:
            await session.ws.send(build_frame("RECEIPT", {"receipt-id": receipt}))
        # El cierre real lo manejará el handler tras salir del loop.


# ----------------------------
# Servidor WebSocket
# ----------------------------

broker = StompBroker()


async def handler(ws: ServerConnection):
    """
    Acepta cualquier path, p.ej.:
      - ws://localhost:8080/ws
      - ws://localhost:8080/chat-websocket/websocket
    """
    session_id = broker.on_connect(ws)
    session = broker.sessions[session_id]

    try:
        async for raw in ws:
            for (command, headers, body) in parse_frames(raw):
                cmd = command.upper()

                if cmd == "CONNECT":
                    await broker.handle_connect(session, headers)

                elif cmd == "SUBSCRIBE":
                    await broker.handle_subscribe(session, headers)

                elif cmd == "SEND":
                    await broker.handle_send(session, headers, body)

                elif cmd == "DISCONNECT":
                    await broker.handle_disconnect(session, headers)
                    # Cerramos el socket luego de atender DISCONNECT
                    await ws.close()
                    break

                else:
                    # Comando no soportado en este mínimo
                    err = build_frame("ERROR", {"message": f"Unsupported command {cmd}"})
                    await ws.send(err)

    except websockets.exceptions.ConnectionClosedOK:
        pass
    except websockets.exceptions.ConnectionClosedError:
        pass
    except Exception as exc:
        logging.exception("Error en handler: %s", exc)
    finally:
        broker.on_disconnect(session_id)


async def main():
    host = "0.0.0.0"
    port = 8080
    async with websockets.serve(handler, host, port):
        logging.info("Servidor STOMP WS escuchando en ws://%s:%d", host, port)
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Apagando servidor...")