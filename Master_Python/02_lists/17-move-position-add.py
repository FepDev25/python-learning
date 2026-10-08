
numbers = [0] * 10

for i in range(len(numbers) - 1):
    numbers[i] = int(input('Ingrese un numero: '))

element = int(input('Nuevo elemento: '))
position = int(input('Posicion donde agregar (0 - 9): '))

for i in range(len(numbers) - 2, position - 1, -1):
    numbers[i + 1] = numbers[i]

numbers[position] = element

print(numbers)