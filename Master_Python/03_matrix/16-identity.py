
matrix = [[ 0 for _ in range(5)] for _ in range(5)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] = 1

for row in matrix:
    for value in row:
        print(value, end='\t')
    print()
