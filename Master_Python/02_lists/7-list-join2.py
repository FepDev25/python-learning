
a = [0] * 12
b = [0] * 12
c = [0] * 24

for i in range(len(a)):
    a[i] = i + 1

for i in range(len(b)):
    b[i] = (i + 1)*5

aux = 0
for i in range(0, len(a), 3):
    for j in range(3):
        c[aux] = a[i + j]
        aux += 1

    for j in range(3):
        c[aux] = b[i + j]
        aux += 1

for i in range(len(c)):
    print(f'{i}: {c[i]}')