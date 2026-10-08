
from array import array

matrix = [
    array('i', [1, 2, 3]),
    array('i', [4, 5, 6]),
    array('i', [7, 8, 9])
]

print(matrix[1][2])

for row in matrix:
    for value in row:
        print(value, end='\t')
    print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='\t')
    print()