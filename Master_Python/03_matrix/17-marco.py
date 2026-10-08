
matrix = [[ 0 for _ in range(5)] for _ in range(5)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i == j
                or i == 0
                or j == 0
                or i == len(matrix) - 1
                or j == len(matrix[0]) - 1):
            matrix[i][j] = 1

for row in matrix:
    for value in row:
        print(value, end='\t')
    print()
