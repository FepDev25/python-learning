import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con layout place")
root.geometry("400x300")  # Tamaño fijo para apreciar mejor las posiciones

# Botón superior (Norte)
btn_north = tk.Button(root, text="Norte", width=10, height=2, command=lambda: print("Norte"))
btn_north.place(relx=0.5, rely=0.0, anchor="n")  # centrado horizontal arriba

# Botón inferior (Sur)
btn_south = tk.Button(root, text="Sur", width=10, height=2, command=lambda: print("Sur"))
btn_south.place(relx=0.5, rely=1.0, anchor="s")  # centrado horizontal abajo

# Botón izquierdo (Oeste)
btn_west = tk.Button(root, text="Oeste", width=10, height=2, command=lambda: print("Oeste"))
btn_west.place(relx=0.0, rely=0.5, anchor="w")  # centrado vertical a la izquierda

# Botón derecho (Este)
btn_east = tk.Button(root, text="Este", width=10, height=2, command=lambda: print("Este"))
btn_east.place(relx=1.0, rely=0.5, anchor="e")  # centrado vertical a la derecha

# Botón central (Centro)
btn_center = tk.Button(root, text="Centro", width=10, height=2, command=lambda: print("Centro"))
btn_center.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()