
def main():

    name = input('Como te llamas? \n')
    age = int(input('Que edad tienes? \n'))
    print(f'Hola, {name}, tienes {age} años')
try:
    main()
except ValueError:
    print('Error: debe introducir un numero entero valido!')
    main()