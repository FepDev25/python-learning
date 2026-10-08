
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print('Matriz Original')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='\t')
    print()

for i in range(1, len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print('Matriz transpuesta')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='\t')
    print()