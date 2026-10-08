import tkinter as tk

root = tk.Tk()
root.title("Botones en Grid 4x3")

# Crear un frame que contendrá los botones
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Crear los 12 botones en un grid 4x3
for i in range(12):
    fila = i // 3     # División entera → determina la fila
    columna = i % 3   # Resto → determina la columna
    boton = tk.Button(frame, text=f"Botón {i+1}", width=12, height=2,
                      command=lambda n=i+1: print(f"Se pulsó el botón {n}"))
    boton.grid(row=fila, column=columna, padx=5, pady=5)
    # boton.bind("<Button-1>", lambda event, n=i+1: print(f"Se pulsó el botón {n}"))

root.mainloop()