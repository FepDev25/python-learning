
a = [''] * 5

for i in range(len(a)):
    a[i] = input('Ingrese un nombre: ').strip()

name = input('Ingrese un nombre a buscar: ').strip()

result = next(((i, n) for i, n in enumerate(a) if n.lower() == name.lower()), (-1, None))
pos, found = result

if pos == -1:
    print('Nombre no encontrado')
else:
    print(f'Encontrado {found} en la posicion: {pos}')