
products = [None] * 7
products[0] = 'Kingston Pendrive 64GB'
products[1] = 'Samsung Galaxy'
products[2] = 'Samsung external ssd drive'
products[3] = 'Asus Notebook'
products[4] = 'Macbook pro'
products[5] = 'Chromecast 4th generation'
products[6] = 'Oxford Bicycle'

products.sort()

prod1 = products[0]
prod2 = products[1]
prod3 = products[2]
prod4 = products[3]
prod5 = products[4]
prod6 = products[5]
prod7 = products[6]

for e in reversed(products):
    print(f' - {e}')

for e in products[::-1]:
    print(f'* {e}')

print(prod1)
print(prod2)
print(prod3)
print(prod4)
print(prod5)
print(prod6)
print(prod7)

# numbers = [0] * 6
# numbers[0] = 1
# numbers[1] = 2
# numbers[2] = 3
# numbers[3] = 4
# numbers[4] = 'Andres'
# numbers[5] = 'Guzman'

numbers = [10, 7, 35, -4, int('6'), int('-1')]
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# numbers.append(4)
# numbers.append('Andres')
# numbers.append('Guzman')

i = numbers[0]
j = numbers[1]
k = numbers[2]
l = numbers[3]
m = numbers[4]
n = numbers[5]

print(f'cantidad de elementos: {len(numbers)}')
print(f'acceder al primero elemento: {numbers[0]}')
print(f'acceder al ultimo elemento: {numbers[len(numbers) - 1]}')
print(f'i = {i}')
print(f'j = {j}')
print(f'k = {k}')
print(f'l = {l}')
print(f'm = {m}')
print(f'indice 3 = {numbers[3]}')

numbers.sort()
for elemento in numbers:
    print(elemento)

for i in range(len(numbers)):
    print(f'Indice {i}: {numbers[i]}')

for e in numbers[::-1]:
    print(e)