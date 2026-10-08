import tkinter as tk
from tkinter import messagebox

# --- Estado principal requerido ---
state = {
    "total": 0.0,        # acumulador
    "operation": None,   # operación pendiente: "+", "-", "*", "/"
    "aux": None          # último operando ingresado
}

# Usaremos result_var como "buffer" de entrada mostrado en la pantalla inferior
root = tk.Tk()
root.title("Calculadora clásica")

expression_var = tk.StringVar(value="")   # pantalla superior (expresión)
result_var = tk.StringVar(value="0")      # pantalla inferior (resultado/entrada actual)

# --- Helpers de conversión (coma en UI) ---
def ui_to_float(text: str) -> float:
    text = (text or "0").strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return 0.0

def float_to_ui(value: float) -> str:
    s = f"{value:.12g}"  # evita notación científica en la mayoría de casos
    return s.replace(".", ",")

def update_screens(expr: str | None = None, res: str | None = None):
    if expr is not None:
        expression_var.set(expr)
    if res is not None:
        result_var.set(res)

# --- Lógica de cálculo ---
def apply_pending_operation():
    """Aplica state['operation'] entre state['total'] y state['aux']."""
    op = state["operation"]
    a = state["total"]
    b = state["aux"]
    if op == "+":
        state["total"] = a + b
    elif op == "-":
        state["total"] = a - b
    elif op == "*":
        state["total"] = a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError
        state["total"] = a / b

# --- Handlers solicitados ---
def handle_digit(st: dict, ch: str):
    """Maneja dígitos y coma. Usa result_var como buffer de entrada."""
    buf = result_var.get()

    if ch == ",":
        if "," not in buf:
            # Si buffer es "0" o vacío, empezamos "0,"
            buf = ("0," if buf in ("", "0") else buf + ",")
    else:
        # dígito 0-9
        if buf == "0":
            buf = ch
        else:
            buf += ch

    update_screens(res=buf)

def handel_op(st: dict, op: str):
    """Maneja la selección de operación (+, -, *, /)."""
    # Consolidar el buffer actual a aux
    buf_val = ui_to_float(result_var.get())
    st["aux"] = buf_val

    try:
        if st["operation"] is None:
            # Primera operación: mover aux a total
            st["total"] = st["aux"]
        else:
            # Ya había una operación pendiente: aplicarla
            apply_pending_operation()
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
        handle_ac(st)
        return

    # Setear nueva operación pendiente
    st["operation"] = op
    # Actualizar pantallas: expresión y limpiar buffer visual a 0
    expr = f"{float_to_ui(st['total'])} {st['operation']}"
    update_screens(expr=expr, res="0")

def handle_equal(st: dict):
    """Resuelve la operación pendiente con el buffer actual."""
    if st["operation"] is None:
        # Nada que calcular
        update_screens(res=result_var.get())
        return

    # Tomar buffer como aux
    st["aux"] = ui_to_float(result_var.get())

    try:
        expr = f"{float_to_ui(st['total'])} {st['operation']} {float_to_ui(st['aux'])} ="
        apply_pending_operation()
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
        handle_ac(st)
        return

    # Limpiar operación pendiente, mostrar total y expresión completa
    st["operation"] = None
    update_screens(expr=expr, res=float_to_ui(st["total"]))

def handle_ac(st: dict):
    """Resetea la calculadora."""
    st["total"] = 0.0
    st["operation"] = None
    st["aux"] = None
    update_screens(expr="", res="0")

# --- UI: pantallas ---
label_expr = tk.Label(root, textvariable=expression_var, anchor="e", justify="right", font=("Arial", 12))
label_expr.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=(8, 2))

label_result = tk.Label(root, textvariable=result_var, anchor="e", justify="right", font=("Arial", 20, "bold"))
label_result.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=8, pady=(0, 8))

for c in range(4):
    root.grid_columnconfigure(c, weight=1)

# --- UI: botonera ---
row_base = 2

# Fila 7 8 9 +
tk.Button(root, text="7", command=lambda: handle_digit(state, "7")).grid(row=row_base+0, column=0, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="8", command=lambda: handle_digit(state, "8")).grid(row=row_base+0, column=1, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="9", command=lambda: handle_digit(state, "9")).grid(row=row_base+0, column=2, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="+", command=lambda: handel_op(state, "+")).grid(row=row_base+0, column=3, sticky="nsew", padx=4, pady=4)

# Fila 4 5 6 -
tk.Button(root, text="4", command=lambda: handle_digit(state, "4")).grid(row=row_base+1, column=0, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="5", command=lambda: handle_digit(state, "5")).grid(row=row_base+1, column=1, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="6", command=lambda: handle_digit(state, "6")).grid(row=row_base+1, column=2, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="-", command=lambda: handel_op(state, "-")).grid(row=row_base+1, column=3, sticky="nsew", padx=4, pady=4)

# Fila 1 2 3 *
tk.Button(root, text="1", command=lambda: handle_digit(state, "1")).grid(row=row_base+2, column=0, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="2", command=lambda: handle_digit(state, "2")).grid(row=row_base+2, column=1, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="3", command=lambda: handle_digit(state, "3")).grid(row=row_base+2, column=2, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="*", command=lambda: handel_op(state, "*")).grid(row=row_base+2, column=3, sticky="nsew", padx=4, pady=4)

# Fila , 0 = /
tk.Button(root, text=",", command=lambda: handle_digit(state, ",")).grid(row=row_base+3, column=0, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="0", command=lambda: handle_digit(state, "0")).grid(row=row_base+3, column=1, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="=", command=lambda: handle_equal(state)).grid(row=row_base+3, column=2, sticky="nsew", padx=4, pady=4)
tk.Button(root, text="/", command=lambda: handel_op(state, "/")).grid(row=row_base+3, column=3, sticky="nsew", padx=4, pady=4)

# Fila AC (ocupa 4 columnas)
tk.Button(root, text="AC", command=lambda: handle_ac(state)).grid(row=row_base+4, column=0, columnspan=4, sticky="nsew", padx=4, pady=6)

# Filas elásticas
for r in range(row_base, row_base + 5):
    root.grid_rowconfigure(r, weight=1)

root.mainloop()