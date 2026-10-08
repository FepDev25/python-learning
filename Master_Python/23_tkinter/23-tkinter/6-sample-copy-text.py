import tkinter as tk

def copy_text():
    text = entry_source.get()
    entry_target.delete(0, tk.END)
    entry_target.insert(0, text)
    print(f"Texto copiado: {text}")

root = tk.Tk()
root.title("Ejemplo copiar texto con grid")
root.geometry("350x150")

# Label y campo de texto origen
tk.Label(root, text="Copiar:").grid(row=0, column=0, padx=10, pady=10)
entry_source = tk.Entry(root, width=25)
entry_source.grid(row=0, column=1, padx=10, pady=10)

# Botón para copiar
button_copy = tk.Button(root, text="Copiar", command=copy_text)
button_copy.grid(row=1, column=0, columnspan=2, pady=5)

# Label y campo destino
tk.Label(root, text="Pegado:").grid(row=2, column=0, padx=10, pady=10)
entry_target = tk.Entry(root, width=25)
entry_target.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()