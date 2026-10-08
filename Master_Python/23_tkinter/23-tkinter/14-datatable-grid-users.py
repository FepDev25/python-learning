import tkinter as tk

root = tk.Tk()
root.title("Tabla de usuarios")

# Datos de ejemplo
users = [
    (1, "Andrés", "Guzmán", "andres@example.com"),
    (2, "María", "López", "maria@example.com"),
    (3, "Carlos", "Pérez", "carlos@example.com"),
    (4, "Laura", "Fernández", "laura@example.com"),
]

# Encabezados
headers = ["Id", "Nombre", "Apellido", "Email"]

# Crear encabezados
for col, header in enumerate(headers):
    lbl = tk.Label(
        root,
        text=header,
        font=("Arial", 11, "bold"),
        borderwidth=1,
        relief="solid",
        width=20,
        anchor="center",
        bg="#d9d9d9"
    )
    lbl.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

# Crear filas de datos
for row_idx, user in enumerate(users, start=1):
    for col_idx, value in enumerate(user):
        lbl = tk.Label(
            root,
            text=value,
            borderwidth=1,
            relief="solid",
            width=20,
            anchor="center"
        )
        lbl.grid(row=row_idx, column=col_idx, sticky="nsew", padx=1, pady=1)

# Hacer las columnas elásticas
for col in range(len(headers)):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()