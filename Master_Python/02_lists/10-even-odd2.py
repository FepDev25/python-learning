
numbers = [0] * 10
evens = []
odds = []
even_count = 0
odd_count = 0

print('Ingrese 10 numeros: ')
for i in range(10):
    numbers[i] = int(input('Ingrese un numero: '))

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])
        even_count += 1
    else:
        odds.append(numbers[i])
        odd_count += 1

print(f'Pares {even_count}')
for i in range(len(evens)):
    print(evens[i])

print(f'Impares {odd_count}')
for i in range(len(odds)):
    print(odds[i])