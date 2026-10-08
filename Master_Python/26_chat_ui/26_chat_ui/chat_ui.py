# chat_ui.py
import json
import queue
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from datetime import datetime
from stomp_client import StompWSClient

# =========================
# Config
# =========================
ENDPOINT_WS = "ws://localhost:8080/ws"
DEST_SUBSCRIBE = "/chat/message"
DEST_SEND = "/app/message"

class ChatApp(tk.Tk):
    """
    UI mínima de cliente de chat (sin conexión aún).
    - Header: campo username + botón Conectar
    - Area de mensajes: ScrolledText de solo lectura
    - Label de estado (vacío por ahora)
    - Footer: campo message + botones Enviar y Cerrar chat
    - Métodos on_connect / on_send / on_close por ahora solo hacen print
    - Tags básicos en el área de mensajes: 'username', 'time', 'text'
    """
    def __init__(self):
        super().__init__()
        self.title("Chat - Cliente")
        self.geometry("680x460")
        self.minsize(560, 420)

        # Variables de UI
        self.client: StompWSClient | None = None
        self.username_var = tk.StringVar()
        self.message_var = tk.StringVar()
        self.status_var = tk.StringVar(value="")  # Estado vacío por ahora
        self._connected = False  # flag de estado
        self._my_color: str | None = None  # color propio

        # Cola para frames entrantes (desde el hilo de red)
        self.incoming = queue.Queue()

        # Layout base (grid)
        self.columnconfigure(0, weight=1)
        # Filas: header (auto), mensajes (expand), estado (auto), footer (auto)
        self.rowconfigure(1, weight=1)

        self._build_header()
        self._build_messages_area()
        self._build_status()
        self._build_footer()

        # Estado inicial: desconectado (ocultar chat y footer)
        self._set_connected_ui(False)

        # Atajos
        self.bind("<Return>", self._enter_to_send)
        self.bind("<Control-w>", lambda e: self.on_close_window())
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)

        # Configuración de tags del área de mensajes
        self._configure_message_tags()

        # Comienza el loop de procesamiento de frames
        self.after(50, self._drain_incoming)


    # -------------------------------
    # Construcción de secciones
    # -------------------------------
    def _build_header(self):
        self.header = ttk.Frame(self, padding=(10, 10, 10, 6))
        self.header.grid(row=0, column=0, sticky="ew")
        self.header.columnconfigure(1, weight=1)

        ttk.Label(self.header, text="Usuario:").grid(row=0, column=0, sticky="w", padx=(0, 6))
        self.username_entry = ttk.Entry(self.header, textvariable=self.username_var)
        self.username_entry.grid(row=0, column=1, sticky="ew")
        self.username_entry.focus()

        self.btn_connect = ttk.Button(self.header, text="Conectar", command=self.on_connect)
        self.btn_connect.grid(row=0, column=2, sticky="e", padx=(8, 0))

    def _build_messages_area(self):
        self.frame_messages = ttk.Frame(self, padding=(10, 0, 10, 0))
        self.frame_messages.grid(row=1, column=0, sticky="nsew")
        self.frame_messages.rowconfigure(0, weight=1)
        self.frame_messages.columnconfigure(0, weight=1)

        self.txt_messages = scrolledtext.ScrolledText(
            self.frame_messages,
            wrap="word",
            height=14,
            state=tk.DISABLED  # siempre controlado por helper
        )
        self.txt_messages.grid(row=0, column=0, sticky="nsew")
        # self.txt_messages.configure(state=tk.DISABLED)

    def _build_status(self):
        self.status_frame = ttk.Frame(self, padding=(10, 4, 10, 4))
        self.status_frame.grid(row=2, column=0, sticky="ew")
        self.status_frame.columnconfigure(0, weight=1)

        self.lbl_status = ttk.Label(self.status_frame, textvariable=self.status_var, anchor="w")
        self.lbl_status.grid(row=0, column=0, sticky="ew")

    def _build_footer(self):
        self.footer = ttk.Frame(self, padding=(10, 8, 10, 10))
        self.footer.grid(row=3, column=0, sticky="ew")
        self.footer.columnconfigure(0, weight=1)

        self.entry_message = ttk.Entry(self.footer, textvariable=self.message_var)
        self.entry_message.grid(row=0, column=0, sticky="ew")
        self.entry_message.bind("<Control-Return>", lambda e: self.on_send())
        self.entry_message.bind("<KeyRelease>", self._on_typing)

        self.btn_send = ttk.Button(self.footer, text="Enviar", command=self.on_send)
        self.btn_send.grid(row=0, column=1, padx=(8, 0))

        self.btn_close = ttk.Button(self.footer, text="Cerrar chat", command=self.on_close)
        self.btn_close.grid(row=0, column=2, padx=(8, 0))

    # -------------------------------
    # Tags y helpers del área de mensajes
    # -------------------------------
    def _configure_message_tags(self):
        self.txt_messages.tag_configure("username", font=("TkDefaultFont", 10, "bold"))
        self.txt_messages.tag_configure("time", font=("TkDefaultFont", 9, "italic"))
        self.txt_messages.tag_configure("text", font=("TkDefaultFont", 10))

    def _append_message(self, text: str):
        """Inserta texto controlando state y hace scroll al final."""
        self.txt_messages.configure(state=tk.NORMAL)
        self.txt_messages.insert(tk.END, text)
        self.txt_messages.insert(tk.END, "\n" + "-" * 60 + "\n")
        self.txt_messages.see(tk.END)
        self.txt_messages.configure(state=tk.DISABLED)

    def _append_chat_message(self, date: str, username: str, text: str, color: str | None = None, is_new_user: bool = False):
        """
        Inserta un mensaje aplicando color solo al @username.
        Formatos:
          - MESSAGE:   "{date} @{username} dice:\n{text}\n"
          - NEW_USER:  "{date} nuevo usuario @{username} se ha conectado!\n"
        """
        self.txt_messages.configure(state=tk.NORMAL)
        self.txt_messages.insert(tk.END, f"{date} ")
        if is_new_user:
            self.txt_messages.insert(tk.END, "nuevo usuario ")
        tag = None
        if color:
            tag = self._get_or_create_color_tag(color)
        self.txt_messages.insert(tk.END, f"@{username}", (tag,) if tag else ())
        if is_new_user:
            self.txt_messages.insert(tk.END, " se ha conectado!\n")
        else:
            self.txt_messages.insert(tk.END, " dice:\n")
            self.txt_messages.insert(tk.END, f"{text}\n")
        self.txt_messages.insert(tk.END, "\n" + "-" * 60 + "\n")
        self.txt_messages.see(tk.END)
        self.txt_messages.configure(state=tk.DISABLED)

    def _get_or_create_color_tag(self, color: str) -> str:
        """Crea (si no existe) y devuelve el nombre de tag para un color dado."""
        tag_name = f"usercolor_{color}"
        try:
            self.txt_messages.tag_configure(tag_name, foreground=color)
        except Exception:
            return ""
        return tag_name
    # -------------------------------
    # Callbacks (por ahora solo print)
    # -------------------------------
    def on_connect(self):
        username = (self.username_var.get() or "").strip()
        if not username:
            messagebox.showerror("Falta usuario", "Debes ingresar un nombre de usuario.")
            return

        # Crear cliente STOMP
        self.client = StompWSClient(host_header="localhost", heartbeat_ms=0)

        def _on_connected():
            # Suscribirse cuando llega CONNECTED
            try:
                self.client.subscribe(DEST_SUBSCRIBE)
                # Suscripción a historial por sesión + solicitud de historial
                session_id = self.client.get_session_id()
                if session_id:
                    self.client.subscribe(f"/chat/history/{session_id}")
                    req = {"sessionId": session_id, "limit": 50}
                    self.client.send("/app/history", json.dumps(req), content_type="application/json")
                # Suscribirse al canal de escritura
                self.client.subscribe("/chat/writing")
                self._append_message("[Sistema] Conectado y suscrito a '/chat/message', '/chat/writing' + historial\n")
                self.status_var.set(f"Conectado como '{username}'")

                # Notificar NUEVO USUARIO al backend
                new_user = {
                    "username": username,
                    "type": "NEW_USER",
                    "date": datetime.now().isoformat(timespec="seconds"),
                }
                self.client.send(DEST_SEND, json.dumps(new_user), content_type="application/json")
            except Exception as e:
                self.incoming.put({"type": "ERROR", "error": str(e)})

        def _on_message(frame: dict):
            """
            Llega MESSAGE del broker. Esperamos body JSON.
            Lo enviamos al hilo UI via Queue.
            """
            self.incoming.put({"type": "FRAME", "frame": frame})

        def _on_error(exc: Exception):
            self.incoming.put({"type": "ERROR", "error": str(exc)})

        # Conexión asíncrona
        try:
            self.client.connect_async(
                ENDPOINT_WS,
                on_connected=_on_connected,
                on_message=_on_message,
                on_error=_on_error,
            )
            self._set_connected_ui(True)
            self.status_var.set(f"Conectado como '{username}'")
            # Mensaje informativo en el área
            now = datetime.now().strftime("%I:%M %p").lstrip("0")
            self._append_message(f"{now} Sistema: Conexión simulada iniciada.\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar conexión: {e}")

    def on_send(self):
        if not self._connected:
            messagebox.showerror("No conectado", "Primero debes conectarte con un nombre de usuario.")
            return

        msg = (self.message_var.get() or "").strip()
        if not msg:
            messagebox.showerror("Mensaje vacío", "Debes escribir un mensaje antes de enviar.")
            return

        payload = {
            "username": (self.username_var.get() or "anon").strip() or "anon",
            "text": msg,
            "date": datetime.now().strftime("%I:%M %p").lstrip("0"),
            "type": "MESSAGE",
        }

        try:
            self.client.send(DEST_SEND, json.dumps(payload), content_type="application/json")
            # Opcional: mostrar inmediatamente lo que enviaste (eco local)
            # pretty = f"{payload['date']} @{payload['username']} dice:\n{payload['text']}\n"
            # self._append_message(pretty)
            # Eco local (con color propio si lo conocemos)
            self._append_chat_message(
                payload["date"],
                payload["username"],
                payload["text"],
                color=self._my_color,
                is_new_user=False,
            )
            self.message_var.set("")
            self.entry_message.focus_set()
        except Exception as e:
            messagebox.showerror("Error al enviar", str(e))
        # Formato: HH:MM AM/PM @username dice:\n message\n\n
        # mensaje con separador
        # line = (
        #     f"{time_str} @{username} dice:\n"
        #     f"{msg}\n"
        #     f"{'-' * 60}\n"  # ← línea divisoria
        # )

        print(f"[on_send] from={payload['username']} text={msg!r}")


    def on_close(self):

        # Desconecta si está activo
        if self.client:
            try:
                self.client.disconnect()
            except Exception:
                pass
            self.client = None

        print("[on_close] estado restaurado (simulado)")
        # Limpiar área de mensajes
        self.txt_messages.configure(state=tk.NORMAL)
        self.txt_messages.delete("1.0", tk.END)
        self.txt_messages.configure(state=tk.DISABLED)
        # Reset de estado/vars
        self.status_var.set("")
        self.message_var.set("")
        self.username_entry.focus()
        self._set_connected_ui(False)

    def on_close_window(self):
        self.on_close()
        self.destroy()
    # -------------------------------
    # Utilidad: Enter para enviar
    # -------------------------------
    def _enter_to_send(self, event):
        # Si el foco está en el entry de mensaje, Enter envía
        if self.focus_get() == self.entry_message:
            self.on_send()

    def _set_connected_ui(self, connected: bool):
        """Habilita o deshabilita secciones según el estado de conexión."""
        self._connected = connected
        if connected:
            # Oculta el header, muestra chat y footer
            # Desactivamos u ocultamos los controles de conexión
            self.username_entry.configure(state=tk.DISABLED)
            self.btn_connect.configure(state=tk.DISABLED)
            # Opcional: ocultar visualmente header de usuario/btn
            self.header.grid_remove()
            self.frame_messages.grid()
            self.footer.grid()
            self.entry_message.configure(state=tk.NORMAL)
            self.btn_send.configure(state=tk.NORMAL)
            self.btn_close.configure(state=tk.NORMAL)
        else:
            # Restaura estado inicial
            self.header.grid()
            self.username_entry.configure(state=tk.NORMAL)
            self.btn_connect.configure(state=tk.NORMAL)
            self.frame_messages.grid_remove()
            self.footer.grid_remove()

    def _on_typing(self, event):
        """Envía un aviso /app/writing con el username cuando el usuario teclea."""
        if not self.client or not self.client.is_connected():
            return
        username = (self.username_var.get() or "Anon").strip()
        try:
            self.client.send("/app/writing", json.dumps({"username": username}), content_type="application/json")
        except Exception:
            pass

    # =========================
    # Procesar cola entrante
    # =========================
    def _drain_incoming(self):
        """
        Saca items de la queue puestos por el hilo de red y los pinta en la UI.
        Llamado periódicamente con after().
        """
        try:
            while True:
                item = self.incoming.get_nowait()
                typ = item.get("type")
                if typ == "ERROR":
                    self._append_message(f"[Error] {item.get('error')}")
                elif typ == "FRAME":
                    frame = item["frame"]
                    cmd = frame.get("command")
                    if cmd == "MESSAGE":
                        body = frame.get("body") or ""
                        try:
                            data = json.loads(body)
                            # ARRAY => historial
                            dest = frame.get("headers", {}).get("destination", "")
                            if isinstance(data, list):
                                for msg in data:
                                    username = (msg.get("username") or "Anon")
                                    text = msg.get("text", "")
                                    date = msg.get("date", datetime.now().isoformat(timespec="seconds"))
                                    color = msg.get("color")
                                    self._append_chat_message(date, username, text, color=color,
                                                              is_new_user=(msg.get("type") == "NEW_USER"))
                            elif dest == "/chat/writing":
                                username = data.get("username", "Alguien")
                                self.status_var.set(f"{username} está escribiendo...")
                                # borrar el texto después de 2 segundos
                                self.after(2000, lambda: self.status_var.set(""))
                            else:
                                # Objeto individual
                                if data.get("type") == "NEW_USER":
                                    username = (data.get("username") or "Anon")
                                    date = data.get("date", datetime.now().isoformat(timespec="seconds"))
                                    color = data.get("color")
                                    # Si es mi propio NEW_USER, guardo mi color
                                    if username == (self.username_var.get() or "").strip():
                                        self._my_color = color
                                    self._append_chat_message(date, username, "", color=color, is_new_user=True)
                                else:
                                    username = (data.get("username") or "Anon")
                                    text = data.get("text", "")
                                    date = data.get("date", datetime.now().isoformat(timespec="seconds"))
                                    color = data.get("color")
                                    self._append_chat_message(date, username, text, color=color, is_new_user=False)
                        except Exception:
                            self._append_message(f"[Mensaje crudo]\n{body}\n")
                    elif cmd == "ERROR":
                        self._append_message(f"[STOMP ERROR] {frame.get('body','')}")
                    else:
                        self._append_message(f"[{cmd}] {frame.get('headers',{})}")
        except queue.Empty:
            pass

        self.after(50, self._drain_incoming)

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()