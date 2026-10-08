
numbers = [0] * 10

for i in range(len(numbers)):
    numbers[i] = int(input('Ingrese un numero: '))

element = int(input('Eliminar elemento: '))

position = next((i for i in range(len(numbers)) if element == numbers[i]), - 1)

if position == -1:
    print('No hay nada que eliminar, no existe el valor en la lista')
    exit(0)

# numbers.remove(6)
for i in range(position, len(numbers) - 1, 1):
    numbers[i] = numbers[i + 1]

new = numbers[:-1]
print('Lista original: ', numbers)
print('Lista nueva: ', new)
