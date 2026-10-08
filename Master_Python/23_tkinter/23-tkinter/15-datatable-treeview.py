import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabla de usuarios con Treeview")

# --- Datos de ejemplo ---
users = [
    (1, "Andrés", "Guzmán", "andres@example.com"),
    (2, "María", "López", "maria@example.com"),
    (3, "Carlos", "Pérez", "carlos@example.com"),
    (4, "Laura", "Fernández", "laura@example.com"),
    (5, "Sofía", "Ramírez", "sofia.ramirez@example.com"),
]

# --- Frame contenedor ---
frame_table = ttk.Frame(root, padding=8)
frame_table.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- Scrollbars ---
scrollbar_y = ttk.Scrollbar(frame_table, orient="vertical")
scrollbar_x = ttk.Scrollbar(frame_table, orient="horizontal")

# --- Treeview ---
columns = ("Id", "Nombre", "Apellido", "Email")
tree = ttk.Treeview(
    frame_table,
    columns=columns,
    show="headings",
    yscrollcommand=scrollbar_y.set,
    xscrollcommand=scrollbar_x.set
)

# Configurar columnas (centradas)
tree.heading("Id", text="Id")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")
tree.heading("Email", text="Email")

tree.column("Id", anchor="center", width=60, stretch=False)
tree.column("Nombre", anchor="center", width=140)
tree.column("Apellido", anchor="center", width=140)
tree.column("Email", anchor="center", width=220)

# Vincular scrollbars
scrollbar_y.config(command=tree.yview)
scrollbar_x.config(command=tree.xview)

# Ubicar en grid
tree.grid(row=0, column=0, sticky="nsew")
scrollbar_y.grid(row=0, column=1, sticky="ns")
scrollbar_x.grid(row=1, column=0, sticky="ew")

# Hacer el frame elástico
frame_table.grid_rowconfigure(0, weight=1)
frame_table.grid_columnconfigure(0, weight=1)

# Insertar datos
for user in users:
    tree.insert("", "end", values=user)

root.mainloop()