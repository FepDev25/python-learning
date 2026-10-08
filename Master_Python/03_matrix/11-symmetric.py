symmetric = True
matrix = [
    [1, 6, 89, 3],
    [6, 1, 0, 9],
    [89, 0, 1, 0],
    [3, 9, 0, 1]
]

for i in range(len(matrix)):
    for j in range(i):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break

if symmetric:
    print('La matrix es simetrica')
else:
    print('La matrix no es simetrica')