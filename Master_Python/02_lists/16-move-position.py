
numbers = [0] * 10

for i in range(len(numbers)):
    numbers[i] = int(input('Ingrese un numero: '))

last = numbers[len(numbers) - 1]

for i in range(len(numbers) - 2, -1, -1):
    numbers[i + 1] = numbers[i]

numbers[0] = last

print(numbers)