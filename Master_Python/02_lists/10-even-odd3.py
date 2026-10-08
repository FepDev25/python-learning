
numbers = []

for i in range(10):
    numbers.append(int(input('Ingrese un numero: ')))

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print('Pares')
print(' - '.join(str(num) for num in evens) )
print('Impares')
print(', '.join(str(num) for num in odds) )