
names = [None] * 3

names[0] = [None] * 2
names[1] = [None] * 2
names[2] = [None] * 2

names[0][0] = 'Andres'
names[0][1] = 'Pepe'
names[1][0] = 'Pepa'
names[1][1] = 'Josefa'
names[2][0] = 'Paco'
names[2][1] = 'Lucas'

print('Iterando usando for: ')
for i in range(len(names)):
    for j in range(len(names[i])):
        print(names[i][j], end='\t')
    print()

print('Iterando con for-each')
for row in names:
    for name in row:
        print(name, end='\t')
    print()