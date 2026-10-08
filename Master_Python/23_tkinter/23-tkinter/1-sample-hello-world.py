import tkinter as tk
from tkinter import messagebox

def on_close():
    respuesta = messagebox.askyesno("Salir", "¿Seguro que quieres cerrar la ventana?")
    if respuesta:
        print('cerrando la ventana ...')
        root.destroy()  # Cierra la ventana
    else:
        pass  # No hace nada, la ventana sigue abierta

# Crear la ventana principal
root = tk.Tk()
root.title("Hola Mundo con Tkinter")

# Crear un label (etiqueta) con texto
label = tk.Label(root, text="¡Hola Mundo!")
label.pack(padx=20, pady=20)

# Asociar el evento de cierre a la función on_close
root.protocol("WM_DELETE_WINDOW", on_close)
# Iniciar el bucle principal
root.mainloop()