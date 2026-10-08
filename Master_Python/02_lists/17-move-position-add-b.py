
numbers = [0] * 10

for i in range(len(numbers)):
    numbers[i] = int(input('Ingrese un numero: '))

element = int(input('Nuevo elemento: '))
position = int(input('Posicion donde agregar (0 - 9): '))
last = numbers[len(numbers) - 1]

for i in range(len(numbers) - 2, position - 1, -1):
    numbers[i + 1] = numbers[i]
new_list = numbers[:] + [0]
new_list[position] = element
new_list[-1] = last

print('Original: ', numbers)
print('Nuevo', new_list)