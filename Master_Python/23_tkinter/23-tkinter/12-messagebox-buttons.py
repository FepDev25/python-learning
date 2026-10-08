import tkinter as tk
from tkinter import messagebox

def show_dialogs():
    # Primer diálogo: Yes / No
    answer1 = messagebox.askyesno("Pregunta 1", "¿Desea continuar con la operación?")
    print("Resultado del primer diálogo:", answer1)

    # Segundo diálogo: Yes / No / Cancel
    answer2 = messagebox.askyesnocancel("Pregunta 2", "¿Desea guardar los cambios antes de salir?")
    print("Resultado del segundo diálogo:", answer2)

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

show_dialogs()

root.destroy()  # Cierra completamente la app