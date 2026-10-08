import tkinter as tk

root = tk.Tk()
root.title("10 Botones con pack horizontal")

# Contenedor para los botones
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Crear 10 botones alineados horizontalmente
for i in range(1, 11):
    btn = tk.Button(frame, text=f"Botón {i}", width=10)
    btn.pack(side=tk.LEFT, padx=5)
    btn.bind("<Button-1>", lambda event, n=i: print(f"Se pulsó el botón {n}"))

root.mainloop()