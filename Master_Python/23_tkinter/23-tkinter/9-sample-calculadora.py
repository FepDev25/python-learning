import tkinter as tk
from tkinter import messagebox

# --- Constantes de operación ---
ADD = "ADD"
SUB = "SUB"
MUL = "MUL"
DIV = "DIV"

root = tk.Tk()
root.title("Calculadora con Menú")

# --- Frame principal ---
frame_main = tk.Frame(root, padx=12, pady=12)
frame_main.pack()

# --- Widgets ---
tk.Label(frame_main, text="Número A:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_a = tk.Entry(frame_main, width=15)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_main, text="Número B:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_b = tk.Entry(frame_main, width=15)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_main, text="Resultado:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_result = tk.Entry(frame_main, width=15, state="readonly")
entry_result.grid(row=2, column=1, padx=5, pady=5)


# --- Funciones ---
def parse_number(entry):
    """Convierte el texto de un Entry a float, mostrando error si no es válido."""
    text = entry.get().strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")
        entry.focus_set()
        entry.select_range(0, tk.END)
        return None


def calculate(operation):
    """Realiza la operación matemática según la constante."""
    a = parse_number(entry_a)
    b = parse_number(entry_b)
    if a is None or b is None:
        return

    try:
        if operation == ADD:
            result = a + b
        elif operation == SUB:
            result = a - b
        elif operation == MUL:
            result = a * b
        elif operation == DIV:
            result = a / b
        else:
            raise ValueError("Operación no válida")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
        return

    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, f"{result:.2f}")
    entry_result.config(state="readonly")


def close_app():
    """Cierra la aplicación."""
    if messagebox.askyesno("Salir", "¿Desea salir de la aplicación?"):
        root.destroy()


# --- Menú ---
menu_bar = tk.Menu(root)

# Menú Operaciones
menu_operations = tk.Menu(menu_bar, tearoff=0)
menu_operations.add_command(label="Sumar", command=lambda: calculate(ADD))
menu_operations.add_command(label="Restar", command=lambda: calculate(SUB))
menu_operations.add_command(label="Multiplicar", command=lambda: calculate(MUL))
menu_operations.add_command(label="Dividir", command=lambda: calculate(DIV))
menu_bar.add_cascade(label="Operaciones", menu=menu_operations)

# Menú Cerrar
menu_exit = tk.Menu(menu_bar, tearoff=0)
menu_exit.add_command(label="Salir", command=close_app)
menu_bar.add_cascade(label="Cerrar", menu=menu_exit)

root.config(menu=menu_bar)
root.mainloop()