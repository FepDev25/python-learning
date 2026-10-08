
a = [''] * 5

for i in range(len(a)):
    a[i] = input('Ingrese un nombre: ')

name = input('Ingrese un nombre a buscar: ')

# pos = 0
# while pos < len(a) and a[pos] != num:
#     pos += 1
pos = -1

for i in range(len(a)):
    if a[i].lower() == name.lower():
        pos = i
        break

if pos == -1:
    print('Nombre no encontrado')
else:
    print(f'Encontrado en la posicion: {pos}')