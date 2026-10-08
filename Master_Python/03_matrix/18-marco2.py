n = 10
matrix = [[ 1 if i == j
                or i == 0
                or j == 0
                or i == n - 1
                or j == n - 1 else 0 for j in range(n)] for i in range(n)]

for row in matrix:
    for value in row:
        print(value, end='\t')
    print()
