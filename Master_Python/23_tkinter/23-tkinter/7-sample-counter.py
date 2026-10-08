import tkinter as tk

root = tk.Tk()
root.title("Contador con IntVar")

# Variable entera controlada por Tkinter
counter = tk.IntVar(value=0)

def increment():
    counter.set(counter.get() + 1)
    print(f"Valor actual: {counter.get()}")

def decrement():
    counter.set(counter.get() - 1)
    print(f"Valor actual: {counter.get()}")

# Label vinculado automáticamente a la variable
label_result = tk.Label(root, textvariable=counter, font=("Arial", 16))
label_result.pack(pady=10)

# Botones
button_count = tk.Button(root, text="Count", width=10, command=increment)
button_count.pack(side=tk.LEFT, padx=10, pady=10)

button_decrement = tk.Button(root, text="Decrement", width=10, command=decrement)
button_decrement.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()