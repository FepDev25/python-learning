from bubble_sort import bubble_sort

products = ['Memoria Kingston', 'Samsung Galaxy',
            'Disco Duro SSD Samsung', 'Asus Notebook',
            'Macbook Air', 'Chromecast', 'Bicicleta Oxford']

bubble_sort(products)
total = len(products)

for i in range(total):
    print(f'para indice {i} : {products[i]}')

numbers = [10, 7, 35, -4, int('6'), int('-1')]

bubble_sort(numbers)

for i in range(len(numbers)):
    print(f'para indice {i} : {numbers[i]}')