
rows = 2
cols = 4

numbers = [[0 for j in range(4)] for i in range(2)]

for i in range(rows):
    for j in range(cols):
        numbers[i][j] = j + 1
        if i == 1:
            numbers[i][j] += 10

for i in range(rows):
    for j in range(cols):
        print(numbers[i][j], end=' ')
    print()

print('Numero de filas: ', len(numbers))
print(f'Numero de columnas: { len(numbers[0])}')
print(f'primer elemento de la matriz: {numbers[0][0]}')
print(f'Ultimo elemento de la matriz: {numbers[len(numbers) -1][len(numbers[len(numbers) -1]) - 2]}')
print(f'Ultimo elemento de la matriz: {numbers[-1][-2]}')
print(f'Ultimo elemento de la matriz: {numbers[1][3]}')

num1 = numbers[0][0]
num2 = numbers[0][1]
num3 = numbers[0][2]
num4 = numbers[0][3]

num5 = numbers[1][0]
num6 = numbers[1][1]
num7 = numbers[1][2]
num8 = numbers[1][3]

print('num1: ', num1)
print('num2: ', num2)
print('num3: ', num3)
print('num4: ', num4)
print('num5: ', num5)
print('num6: ', num6)
print('num7: ', num7)
print('num8: ', num8)