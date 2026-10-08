
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

add = [[ a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

for row in add:
    print('\t'.join(str(value) for value in row))