
numbers = []

print('Ingrese 7 numeros: ')
for i in range(7):
    num = int(input(f'Valor {i + 1}: '))
    numbers.append(num)

is_asc = False
is_desc = False

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_desc = True
    if numbers[i] < numbers[i + 1]:
        is_asc = True

if is_asc and is_desc:
    print('Lista desordenada')
elif not is_asc and not is_desc:
    print('Lista con elementos iguales')
elif is_asc and not is_desc:
    print('Lista ordenada de forma ascendente')
elif is_desc and not is_asc:
    print('Lista ordenada de forma descendente')