import tkinter as tk

def custom_dialog(parent):
    # Crear ventana modal
    dialog = tk.Toplevel(parent)
    dialog.title("Confirmación")
    dialog.geometry("600x150")
    dialog.resizable(True, False)
    dialog.grab_set()  # Hace la ventana modal (bloquea la principal)

    tk.Label(dialog, text="¿Desea continuar?", font=("Arial", 12)).pack(pady=20)

    result = {"value": None}

    def set_result(value):
        result["value"] = value
        dialog.destroy()

    # Botones personalizados con valores distintos
    frame = tk.Frame(dialog)
    frame.pack(pady=10)

    buttons = [
        ("No", 0),
        ("Ok / Sí", 1),
        ("Quizás más tarde", 2),
        ("Cancelar", 3),
        ("Otro", 4),
    ]

    for text, val in buttons:
        tk.Button(frame, text=text, width=14, command=lambda v=val: set_result(v)).pack(side=tk.LEFT, padx=3)

    # Esperar hasta que el diálogo se cierre
    dialog.wait_window()
    return result["value"]

# Ventana principal
root = tk.Tk()
root.title("Ventana principal")
root.geometry("300x100")

# Botón para mostrar el diálogo
tk.Button(root, text="Mostrar diálogo", command=lambda: print("Resultado:", custom_dialog(root))).pack(pady=20)

root.mainloop()