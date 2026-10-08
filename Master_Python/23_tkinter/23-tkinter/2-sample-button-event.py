import platform
import tkinter as tk

# Solo en Windows. En Linux/macOS usa bell().
is_windows = platform.system() == "Windows"
if is_windows:
    import winsound

def first_listener(event):
    print("Listener 1: ¡Botón pulsado!")

def second_listener(event):
    print("Listener 2: ¡Click detectado correctamente!")

def third_listener(event):
    print("Listener 3: ¡Ejecutando beep!")

    if is_windows:
        # Beep corto en Windows
        winsound.Beep(800, 200)
    else:
        # Alternativa multiplataforma
        root.bell()

# Crear la ventana principal
root = tk.Tk()
root.geometry('300x400')
root.title("Ejemplo de múltiples eventos")

# Crear un botón
button = tk.Button(root, text="Aceptar", width=15, height=2)
button.pack(padx=20, pady=20)

# Asignar múltiples eventos al mismo clic
button.bind("<Button-1>", first_listener)
button.bind("<Button-1>", second_listener, add="+")  # add="+" permite acumular eventos
button.bind("<Button-1>", third_listener, add="+")

# Iniciar la app
root.mainloop()