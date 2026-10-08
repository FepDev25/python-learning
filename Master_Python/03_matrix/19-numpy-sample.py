
import numpy as np

identity = np.identity(5, dtype=int)
print('Matriz Identity: \n', identity)

random_array = np.random.rand(5)
print(random_array)

random_matrix = np.random.random((5,5))
print(random_matrix)

random_int = np.random.randint(1, 10, size=(5, 5))
print(random_int)

print('Transpuesta: \n', random_int.T)
print('Transpuesta: \n', np.transpose(random_int))

empty = np.zeros((3, 3), dtype=int)
print('Matriz empty 3x3: \n', empty)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)
print(matrix[1, 2])
print('Sumar toda la matriz: ', matrix.sum())
print('Sumar la fila 0: ', matrix[0].sum())
print('Sumar la columna 1: ', matrix[:, 1].sum())
print('Sumar la columna 2: ', matrix[:, 2].sum())