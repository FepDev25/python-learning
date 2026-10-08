import tkinter as tk
from tkinter import messagebox

def open_user_dialog(parent):
    # --- Crear ventana modal ---
    dialog = tk.Toplevel(parent)
    dialog.title("Crear usuario")
    dialog.transient(parent)   # se asocia visualmente al padre
    dialog.grab_set()          # modal: bloquea interacción con el padre

    # --- Variables del formulario ---
    name_var = tk.StringVar()
    lastname_var = tk.StringVar()
    email_var = tk.StringVar()
    role_var = tk.StringVar(value="User")  # valor por defecto

    # --- Formulario con grid ---
    tk.Label(dialog, text="Nombre:").grid(row=0, column=0, sticky="e", padx=8, pady=6)
    entry_name = tk.Entry(dialog, textvariable=name_var, width=28)
    entry_name.grid(row=0, column=1, sticky="w", padx=8, pady=6)

    tk.Label(dialog, text="Apellido:").grid(row=1, column=0, sticky="e", padx=8, pady=6)
    entry_lastname = tk.Entry(dialog, textvariable=lastname_var, width=28)
    entry_lastname.grid(row=1, column=1, sticky="w", padx=8, pady=6)

    tk.Label(dialog, text="Email:").grid(row=2, column=0, sticky="e", padx=8, pady=6)
    entry_email = tk.Entry(dialog, textvariable=email_var, width=28)
    entry_email.grid(row=2, column=1, sticky="w", padx=8, pady=6)

    tk.Label(dialog, text="Rol:").grid(row=3, column=0, sticky="e", padx=8, pady=6)
    role_frame = tk.Frame(dialog)
    role_frame.grid(row=3, column=1, sticky="w", padx=8, pady=6)
    tk.Radiobutton(role_frame, text="Admin", variable=role_var, value="Admin").pack(side=tk.LEFT, padx=4)
    tk.Radiobutton(role_frame, text="User",  variable=role_var, value="User").pack(side=tk.LEFT, padx=4)

    # --- Acciones ---
    def on_ok():
        user_data = {
            "nombre": name_var.get().strip(),
            "apellido": lastname_var.get().strip(),
            "email": email_var.get().strip(),
            "rol": role_var.get()
        }
        # imprime en consola
        print("Usuario creado:", user_data)
        messagebox.showinfo("Éxito", "¡Ejecutado con éxito!")
        dialog.destroy()

    def on_cancel():
        messagebox.showerror("Cancelado", "Operación cancelada por el usuario.")
        dialog.destroy()

    # --- Botonera con pack ---
    buttons_frame = tk.Frame(dialog)
    buttons_frame.grid(row=4, column=0, columnspan=2, pady=(10, 8))
    tk.Button(buttons_frame, text="OK", width=12, command=on_ok).pack(side=tk.LEFT, padx=6)
    tk.Button(buttons_frame, text="Cancelar", width=12, command=on_cancel).pack(side=tk.LEFT, padx=6)

    # Enfoque inicial y tamaño adaptable
    entry_name.focus()
    dialog.columnconfigure(1, weight=1)

    # Espera hasta que se cierre (modal real)
    parent.wait_window(dialog)

# --- Ventana principal ---
root = tk.Tk()
root.title("Ventana principal")
root.geometry("320x160")

tk.Button(root, text="Crear usuario", width=18, command=lambda: open_user_dialog(root)).pack(expand=True, pady=30)

root.mainloop()