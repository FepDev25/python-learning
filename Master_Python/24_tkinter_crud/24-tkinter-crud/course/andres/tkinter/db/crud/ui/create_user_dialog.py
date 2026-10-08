from __future__ import annotations

import re
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional

from course.andres.tkinter.db.crud.models.user import User
from course.andres.tkinter.db.crud.repositories.user_repository import UserRepository


class CreateUserDialog(tk.Toplevel):
    """
    Modal para crear un nuevo usuario.
    Campos: name, username, email, password.
    """
    EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, parent: tk.Tk, repo: UserRepository, user: Optional[User] = None):
        super().__init__(parent)
        self.repo = repo
        self.user = user  # puede ser None
        self.editing = bool(user and getattr(user, "id", 0) and int(user.id) > 0)
        self.created_user: Optional[User] = None
        self.title("Edit User" if self.editing else "Create User")
        self.transient(parent)
        self.resizable(False, False)

        self._build_form()
        self._center_to_parent(parent)

        # Modal
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.on_cancel)
        if self.editing:
            self._populate_from_user(user)

    def _build_form(self):
        frm = ttk.Frame(self, padding=12)
        frm.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frm, text="Name *").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 6))
        ttk.Label(frm, text="Username *").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=6)
        ttk.Label(frm, text="Email *").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=6)
        ttk.Label(frm, text="Password *").grid(row=3, column=0, sticky="w", padx=(0, 8), pady=6)

        self.var_id = tk.IntVar(value=(int(self.user.id) if self.editing else 0))
        self.var_name = tk.StringVar()
        self.var_username = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_password = tk.StringVar()

        e1 = ttk.Entry(frm, textvariable=self.var_name, width=36)
        e2 = ttk.Entry(frm, textvariable=self.var_username, width=36)
        e3 = ttk.Entry(frm, textvariable=self.var_email, width=36)
        e4 = ttk.Entry(frm, textvariable=self.var_password, width=36, show="•")

        e1.grid(row=0, column=1, pady=(0, 6))
        e2.grid(row=1, column=1, pady=6)
        e3.grid(row=2, column=1, pady=6)
        e4.grid(row=3, column=1, pady=6)

        # Botones
        btns = ttk.Frame(frm)
        btns.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(btns, text="Cancel", command=self.on_cancel).grid(row=0, column=0, padx=(0, 8))
        ttk.Button(btns, text=("Update" if self.editing else "Save"), command=self.on_save).grid(row=0, column=1)

        # Enter para guardar, Esc para cancelar
        self.bind("<Return>", lambda _: self.on_save())
        self.bind("<Escape>", lambda _: self.on_cancel())

        # Foco inicial
        e1.focus_set()

    def _populate_from_user(self, user: User):
        self.var_name.set(user.name or "")
        self.var_username.set(user.username or "")
        self.var_email.set(user.email or "")
        # no exponemos el password real
        self.var_password.set("")

    def _center_to_parent(self, parent: tk.Tk):
        self.update_idletasks()
        pw = parent.winfo_width()
        ph = parent.winfo_height()
        px = parent.winfo_rootx()
        py = parent.winfo_rooty()

        w = self.winfo_width()
        h = self.winfo_height()
        x = px + (pw - w) // 2
        y = py + (ph - h) // 2
        self.geometry(f"+{x}+{y}")

    # --------- Actions ---------
    def on_cancel(self):
        self.created_user = None
        self.destroy()

    def on_save(self):
        name = self.var_name.get().strip()
        username = self.var_username.get().strip()
        email = self.var_email.get().strip()
        password = self.var_password.get().strip()
        id_val = int(self.var_id.get() or 0)

        # Validaciones mínimas
        if not name or not username or not email:
            messagebox.showwarning("Validation", "Name, Username and Email are required.")
            return
        if not CreateUserDialog.EMAIL_RE.match(email):
            messagebox.showwarning("Validation", "Invalid email format.")
            return
        if id_val <= 0 and not password:
            messagebox.showwarning("Validation", "Password is required for creation.")
            return

        try:
            # Bandera de update/insert: id > 0 => UPDATE, si no => INSERT
            if id_val > 0:
                user = User(
                    id=id_val,
                    name=name,
                    username=username,
                    email=email,
                    password=(password if password else (self.user.password if self.user else "")),
                )
            else:
                user = User(
                    name=name,
                    username=username,
                    email=email,
                    password=password,
                )
            created = self.repo.save(user)
            self.created_user = created
            messagebox.showinfo("Success", "User updated." if id_val > 0 else f"User created (id={created.id}).")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create user:\n{e}")
