
names = []

names.append([])
names.append([])
names.append([])

names[0].append('Andres')
names[0].append('Pepe')
names[1].append('Pepa')
names[1].append('Josefa')
names[2].append('Paco')
names[2].append('Lucas')

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