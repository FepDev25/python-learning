symmetric = True
matrix = [
    [1, 2, 3, 4],
    [2, 1, 0, 5],
    [3, 0, 1, 6],
    [4, 5, 6, 7]
]

i = 0
while i < len(matrix) and symmetric:
    j = 0
    while j < i:
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
        j += 1
    i+=1

if symmetric:
    print('La matrix es simetrica')
else:
    print('La matrix no es simetrica')