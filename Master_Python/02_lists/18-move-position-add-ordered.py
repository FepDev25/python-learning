
numbers = [0] * 7

for i in range(len(numbers) - 1):
    numbers[i] = int(input('Ingrese un numero: '))

element = int(input('Nuevo elemento: '))

position = next((i for i in range(len(numbers) - 1) if element <= numbers[i]), len(numbers) - 1)

for i in range(len(numbers) - 2, position - 1, -1):
    numbers[i + 1] = numbers[i]

numbers[position] = element

print(numbers)