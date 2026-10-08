
rows = 4
cols = 3
# matrix = []

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(i * cols + j + 1)
#     matrix.append(row)

matrix = [[i * cols + j + 1 for j in range(cols) ] for i in range(rows)]

matrix[1][1] = 22
matrix[-2][-1] = 21

print(matrix[-1][-2])
print()
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()