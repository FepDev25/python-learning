import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal mientras se muestran los diálogos

# Mensaje de error
messagebox.showerror("Error de entrada", "Debe introducir datos en los campos!")

# Mensaje de advertencia
messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

# Mensaje de éxito (usamos showinfo para mensajes informativos)
messagebox.showinfo("Éxito", "Operación realizada correctamente.")

root.deiconify()  # Muestra la ventana principal al final (opcional)
root.title("Ventana principal")
root.geometry("300x200")

tk.Label(root, text="Ventana principal activa", font=("Arial", 12)).pack(expand=True)

root.mainloop()