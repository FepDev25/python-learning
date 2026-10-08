flag = True
numbers = []

while flag:
    num = int(input('Ingrese un numero: '))
    numbers.append(num)
    flag = True if input('Ingrese Si para continuar: ').lower() == 'si' else False

max = 0
for num in numbers:
    max = max if max > num else num

print(f'El numero mayor es {max}')