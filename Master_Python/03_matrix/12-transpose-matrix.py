
a = [[(i + j) * 3 for j in range(4)] for i in range(8)]
b = [[0 for _ in range(8)] for _ in range(4)]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='\t')
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        b[j][i] = a[i][j]

print('La matrix transpuesta b:')
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end='\t')
    print()