from __future__ import annotations
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import Optional

from course.andres.tkinter.db.crud.models.user import User
from course.andres.tkinter.db.crud.repositories.user_repository import UserRepository
from course.andres.tkinter.db.crud.ui.create_user_dialog import CreateUserDialog


class UsersApp(tk.Tk):
    def __init__(self, repo: UserRepository):
        super().__init__()
        self.title("Users - List")
        self.geometry("1024x600")
        self.repo = repo
        self._all_users = []  # cache para filtrado local

        self._build_ui()
        self._configure_grid()
        self.load_users()

    # ---------- UI ----------
    def _build_ui(self):
        # Barra superior: búsqueda + botones
        top = ttk.Frame(self, padding=(8, 8, 8, 4))
        top.grid(row=0, column=0, sticky="ew")
        top.columnconfigure(1, weight=1)

        ttk.Label(top, text="Search:").grid(row=0, column=0, padx=(0, 8))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.apply_filter())
        self.search_entry = ttk.Entry(top, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, sticky="ew", padx=(0, 8))
        ttk.Button(top, text="Refresh", command=self.load_users).grid(row=0, column=2)
        ttk.Button(top, text="Clear", command=lambda: self.search_var.set("")).grid(row=0, column=3, padx=(8, 0))
        ttk.Button(top, text="New User", command=self.open_create_dialog).grid(row=0, column=4)

        # Treeview + scrollbars
        middle = ttk.Frame(self, padding=(8, 4, 8, 8))
        middle.grid(row=1, column=0, sticky="nsew")
        middle.rowconfigure(0, weight=1)
        middle.columnconfigure(0, weight=1)

        columns = ("id", "name", "username", "email", "created_at", "delete", "edit")
        self.tree = ttk.Treeview(middle, columns=columns, show="headings", selectmode="browse")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbars
        vsb = ttk.Scrollbar(middle, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(middle, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Encabezados y anchos
        self.tree.heading("id", text="ID", command=lambda: self.sort_by("id", as_number=True))
        self.tree.heading("name", text="Name", command=lambda: self.sort_by("name"))
        self.tree.heading("username", text="Username", command=lambda: self.sort_by("username"))
        self.tree.heading("email", text="Email", command=lambda: self.sort_by("email"))
        self.tree.heading("created_at", text="Created At", command=lambda: self.sort_by("created_at"))
        self.tree.heading("delete", text="Delete")  # columna del “botón”
        self.tree.heading("edit", text="Edit")  # columna del “botón”

        self.tree.column("id", width=80, anchor="center")
        self.tree.column("name", width=180, anchor="w")
        self.tree.column("username", width=140, anchor="w")
        self.tree.column("email", width=220, anchor="w")
        self.tree.column("created_at", width=160, anchor="center")
        self.tree.column("delete", width=100, anchor="center", stretch=False)
        self.tree.column("edit", width=100, anchor="center", stretch=False)

        # Estilos alternados
        style = ttk.Style(self)
        style.configure("Treeview", rowheight=24)
        self.tree.tag_configure("odd", background="#999999")
        self.tree.tag_configure("even", background="#444444")

        # Doble clic para ver detalle
        self.tree.bind("<Double-1>", self.on_double_click)
        # Eventos: clic y hover para cursor “mano” en columna action
        self.tree.bind("<Button-1>", self.on_click_tree)
        self.tree.bind("<Motion>", self.on_motion_tree)
        self._delete_col_index = self.tree["columns"].index("delete") + 1  # 1-based para identify_column
        self._edit_col_index = self.tree["columns"].index("edit") + 1  # 1-based para identify_column

    def _configure_grid(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    # ---------- Data ----------
    def load_users(self):
        try:
            users = self.repo.find_all()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load users:\n{e}")
            return
        self._all_users = users
        self._populate_tree(users)

    def _populate_tree(self, users):
        self.tree.delete(*self.tree.get_children())
        for idx, u in enumerate(users):
            created = self._fmt_dt(getattr(u, "created_at", None))
            row = (u.id, u.name, u.username, u.email, created, "Eliminar", 'Editar')
            tag = "odd" if idx % 2 else "even"
            self.tree.insert("", "end", values=row, tags=(tag,))

    def apply_filter(self):
        q = self.search_var.get().strip()
        try:
            if not q:
                # sin término => listar todo desde la BBDD
                users = self.repo.find_all()
            else:
                users = self.repo.search(q)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search users:\n{e}")
            return

        # opcional: mantener una caché en memoria si la sigues usando para otras cosas
        self._all_users = users
        self._populate_tree(users)

    def apply_filter_programmatic(self):
        q = self.search_var.get().strip().lower()
        if not q:
            self._populate_tree(self._all_users)
            return
        # Filtrado local por name/username/email
        filtered = [
            u for u in self._all_users
            if q in (u.name or "").lower()
            or q in (u.username or "").lower()
            or q in (u.email or "").lower()
        ]
        self._populate_tree(filtered)

    # ---------- Helpers ----------
    # ------------- Create Modal -------------
    def open_create_dialog(self, user: Optional[User] = None):
        dlg = CreateUserDialog(self, self.repo, user)
        self.wait_window(dlg)  # bloquea hasta que se cierre
        if getattr(dlg, "created_user", None):
            self.load_users()  # refresca tabla
            # Opcional: seleccionar el recién creado
            created_id = dlg.created_user.id
            for item in self.tree.get_children():
                if str(self.tree.item(item, "values")[0]) == str(created_id):
                    self.tree.selection_set(item)
                    self.tree.see(item)
                    break

    @staticmethod
    def _fmt_dt(dt):
        if not dt:
            return ""
        # dt puede venir como datetime o string; normalizamos
        if isinstance(dt, datetime):
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        try:
            return str(dt)
        except Exception:
            return ""

    def sort_by(self, field: str, as_number: bool = False):
        # Ordena usando el contenido actual del tree (estable) y re-renderiza
        rows = [self.tree.item(i)["values"] for i in self.tree.get_children("")]
        col_index = {"id": 0, "name": 1, "username": 2, "email": 3, "created_at": 4}[field]

        def key_fn(v):
            val = v[col_index]
            if as_number:
                try:
                    return int(val)
                except Exception:
                    return float("inf")
            return str(val).lower()

        # Toggle asc/desc por columna
        current = getattr(self, "_sort_state", {})
        ascending = not current.get(field, True)
        rows.sort(key=key_fn, reverse=ascending)
        self._sort_state = {field: ascending}

        # Re-pintar con el nuevo orden
        self.tree.delete(*self.tree.get_children())
        for idx, r in enumerate(rows):
            tag = "odd" if idx % 2 else "even"
            self.tree.insert("", "end", values=r, tags=(tag,))

    def on_double_click(self, _event):
        item = self.tree.focus()
        if not item:
            return
        vals = self.tree.item(item, "values")
        # vals: (id, name, username, email, created_at)
        messagebox.showinfo(
            "User detail",
            f"ID: {vals[0]}\nName: {vals[1]}\nUsername: {vals[2]}\nEmail: {vals[3]}\nCreated: {vals[4]}"
        )

    # -------- Interacciones (botón 'Eliminar' por fila) --------
    def on_motion_tree(self, event: tk.Event):
        """Cambia el cursor a 'hand2' si el mouse está sobre la columna action."""
        col = self.tree.identify_column(event.x)  # '#1', '#2', ...
        if col == f"#{self._delete_col_index}" or col == f"#{self._edit_col_index}":
            self.tree.configure(cursor="hand2")
        else:
            self.tree.configure(cursor="")

    def on_click_tree(self, event: tk.Event):
        """Si se hace clic en la columna 'action', confirmar y eliminar."""
        item = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)  # '#1'..'#N'
        if not item or col not in (f"#{self._delete_col_index}", f"#{self._edit_col_index}"):
            return

        vals = self.tree.item(item, "values")  # (id, name, username, email, created_at, 'Eliminar')
        if not vals:
            return

        # Edit
        if col == f"#{self._edit_col_index}":
           user_id = int(vals[0])
           user_obj = next((u for u in self._all_users if int(u.id) == user_id), None)
           self.open_create_dialog(user_obj)
           return

        # Delete
        if col == f"#{self._delete_col_index}":
           self._handle_delete(item, vals)
           return

    def _handle_delete(self, item, vals):
        user_id = vals[0]
        username = vals[2]

        if not messagebox.askyesno("Confirm delete", f"Delete user '{username}' (id={user_id})?"):
            return

        # 1) Borrar en BBDD
        try:
            deleted = self.repo.remove(int(user_id))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete user:\n{e}")
            return

        if not deleted:
            messagebox.showinfo("Info", "User not found or could not be deleted.")
            return

        # 2) Quitar fila del Treeview
        self.tree.delete(item)
        # 3) Actualizar caché local
        self._all_users = [u for u in self._all_users if str(u.id) != str(user_id)]
