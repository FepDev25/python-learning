
numbers = [0] * 10
even_count = 0
odd_count = 0

print('Ingrese 10 numeros: ')
for i in range(10):
    numbers[i] = int(input('Ingrese un numero: '))

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

evens = [0] * even_count
odds = [0] * odd_count

j = 0
k = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens[j] = numbers[i]
        j += 1
    else:
        odds[k] = numbers[i]
        k += 1

print(f'Pares {even_count}')
for i in range(len(evens)):
    print(evens[i])

print(f'Impares {odd_count}')
for i in range(len(odds)):
    print(odds[i])