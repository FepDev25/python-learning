
import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

y = np.random.randint(0, 10, size=(3, 3))
print(x)
print(y)

print('Sumar: \n', np.add(x, y))
print('Restar: \n', np.subtract(x, y))
print('Multiplicar: \n', np.multiply(x, y))
print('Dividir: \n', np.divide(x, y))

new_matrix = np.delete(x, 0, axis=0)
new_matrix2 = np.delete(x, 2, axis=1)
print('Eliminar Fila 0: \n', new_matrix)
print('Eliminar Columna 2: \n', new_matrix2)