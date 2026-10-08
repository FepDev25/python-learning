

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))
num3 = int(input('Ingrese un tercer numero: '))
num4 = int(input('Ingrese un cuarto numero: '))

numbers = [num1, num2, num3, num4]
max = 0

for num in numbers:
    max = max if max > num else num

print(f'El numero mayor es {max}')