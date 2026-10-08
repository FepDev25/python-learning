
products = ['Memoria Kingston', 'Samsung Galaxy',
            'Disco Duro SSD Samsung', 'Asus Notebook',
            'Macbook Air', 'Chromecast', 'Bicicleta Oxford']

total = len(products)
count = 0
for i in range(total):
    for j in range(total):
        if products[i].__lt__(products[j]):
            products[i], products[j] = products[j], products[i]
        count += 1

print(f'Contador: {count}')
for i in range(total):
    print(f'para indice {i} : {products[i]}')