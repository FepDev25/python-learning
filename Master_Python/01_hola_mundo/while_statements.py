
print('================ while')
i = 0
while i <= 5:
    print(f'Contador es: {i}')
    i += 1

print('================ while list')
names = ['Andres', 'Luna', 'Juan', 'Margarita', 'Pedro']
count = 0
# print(len('andres'))
while count < len(names):
    print(f'Nombre en posicion {count}: {names[count]}')
    count += 1

print('================ do while')
i = 0
while True:
    print(i)
    i += 1
    if i >= 10:
        break

print('================ do while ejemplo practico')

correct_number = 7

while True:
    attempt = int(input('Adivina el numero: '))
    if attempt == correct_number:
        print('Correcto! has adivinado el numero!')
        break
    else:
        print('Incorrecto, intenta de nuevo!')
