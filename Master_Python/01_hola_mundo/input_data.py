
def main():
    name = input('Introduce el nombre del producto: ')
    # print(f'Producto, {name}')

    price = int(input('Introduce el precio del producto en pesos: '))
    # print(f'El valor final {price} pesos')

    weight = float(input('Ingresa el peso en gramos: '))
    # print(f'Pesa {weight} gramos.')
    print(f'Producto: {name} \nPrecio: {price} USD \nPeso: {weight} gramos')



try:
    main()
except ValueError:
    print('Error: debes introducir bien los datos, decimal es con punto!')
    main()