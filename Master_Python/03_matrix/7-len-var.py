
matrix = [None] * 3

matrix[0] = [0] * 2
matrix[1] = [0] * 3
matrix[2] = [0] * 4

print('Matriz length: ', len(matrix))
print('Fila 0 length: ', len(matrix[0]))
print('Fila 1 length: ', len(matrix[1]))
print('Fila 2 length: ', len(matrix[2]))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = i * j

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='\t')
    print()