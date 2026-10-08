
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(a)):

    row_sum = 0
    col_sum = 0

    for j in range(len(a[0])):
        row_sum += a[i][j]
        col_sum += a[j][i]
    print(f'Total row {i}: {row_sum}')
    print(f'Total column {i}: {col_sum}')