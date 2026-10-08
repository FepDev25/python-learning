
age = 18

message = 'Mayor de edad' if age >= 18 else 'Menor de edad'
print(message)

math = float(input('Ingrese la nota de matematicas entre 2.00 y 7.0: '))
sciences = float(input('Ingrese la nota de ciencias 2.00 - 7: '))
history = float(input('Ingrese la nota de historia: '))

grade = (math + sciences + history) / 3
print(f'Promedio = {grade}')

state = 'Aprobado' if grade >= 4.99 else 'Reprobado'
print(f'Estado = {state}')

# if grade >= 4.99:
#     print('Aprobado')
# else:
#     print('Rechazado')