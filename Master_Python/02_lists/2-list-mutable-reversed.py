
products = ['Memoria Kingston', 'Samsung Galaxy',
            'Disco Duro SSD Samsung', 'Asus Notebook',
            'Macbook Air', 'Chromecast', 'Bicicleta Oxford']

total = len(products)
print(f'total: {total}')
# products.reverse()

for i in range(total // 2):
    current = products[i]
    reverse = products[total-1-i]
    products[i] = reverse
    products[total - 1 - i] = current

for i in range(total):
    print(f'para indice {i} : {products[i]}')