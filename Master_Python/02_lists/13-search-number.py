
a = [0] * 10

for i in range(len(a)):
    a[i] = int(input('Ingrese un numero: '))

num = int(input('Ingrese un numero a buscar: '))

# pos = 0
# while pos < len(a) and a[pos] != num:
#     pos += 1
pos = -1

for i in range(len(a)):
    if a[i] == num:
        pos = i
        break

if pos == -1:
    print('Numero no encontrado')
else:
    print(f'Encontrado en la posicion: {pos}')