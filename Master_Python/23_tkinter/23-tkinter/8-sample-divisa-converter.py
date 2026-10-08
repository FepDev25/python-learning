import tkinter as tk
from tkinter import messagebox

# --- Constantes ---
CURRENCY_EUR = "EUR"
CURRENCY_USD = "USD"
RATE_EUR = 1029.19
RATE_USD = 976.38
COLOR_EUR = "#d6f5d6"  # verde
COLOR_USD = "#cfe8ff"  # azul

root = tk.Tk()
root.title("Conversor de Monedas")

# Frame principal
frame_main = tk.Frame(root, padx=12, pady=12)
frame_main.pack(fill="both", expand=True)

original_bg = frame_main.cget("bg")

# Widgets
tk.Label(frame_main, text="Monto:").grid(row=0, column=0, sticky="w")
entry_amount = tk.Entry(frame_main, width=18)
entry_amount.grid(row=0, column=1, padx=6, pady=4)
entry_amount.focus()

tk.Label(frame_main, text="Resultado:").grid(row=1, column=0, sticky="w")
result_var = tk.StringVar(value="—")
tk.Label(frame_main, textvariable=result_var).grid(row=1, column=1, sticky="w", padx=6, pady=4)


# --- Funciones ---
def parse_amount():
    """Convierte el texto del Entry en número flotante."""
    text = entry_amount.get().strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un monto válido (número).")
        entry_amount.focus_set()
        entry_amount.select_range(0, tk.END)
        return None


def convert_currency(currency_type):
    """Convierte el monto según la moneda indicada."""
    amount = parse_amount()
    if amount is None:
        return

    if currency_type == CURRENCY_EUR:
        rate = RATE_EUR
        color = COLOR_EUR
        symbol = "€"
        label = "EUR"
    else:
        rate = RATE_USD
        color = COLOR_USD
        symbol = "$"
        label = "USD"

    converted = amount / rate
    result_var.set(f"{symbol}{converted:.2f} {label}")
    frame_main.configure(bg=color)


def reset_view():
    """Restaura el estado original."""
    entry_amount.delete(0, tk.END)
    result_var.set("—")
    frame_main.configure(bg=original_bg)
    entry_amount.focus()


# --- Botones ---
tk.Button(frame_main, text="Euros", width=10, command=lambda: convert_currency(CURRENCY_EUR)).grid(row=2, column=0, pady=10)
tk.Button(frame_main, text="Dólar", width=10, command=lambda: convert_currency(CURRENCY_USD)).grid(row=2, column=1, pady=10)
tk.Button(frame_main, text="Reset", width=10, command=reset_view).grid(row=2, column=2, padx=6, pady=10)

# Ajuste de columnas
for col in range(3):
    frame_main.grid_columnconfigure(col, weight=1)

root.mainloop()