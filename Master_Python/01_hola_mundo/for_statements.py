

for element in range(5):
    print(element)

print('============ inicia en dos e incrementa en 2')
for i in range(2, 10, 2):
    print(i)

print('============ decremento ')
for i in range(10, 0, -1):
    print(i)

print('===============')
for i in range(10, -1, -1):
    print(i)

print('============== iterar list')
names = ['Andres', 'Pepe', 'John', 'Juan', '1000', '3.1415']
for name in names:
    print(name)

print('========== iterar string name')
for name in names:
    for char in name:
        print(char)

print('============ iterar string email')
email = 'andres.correo@hotmail.com'
for c in email:
    print(c)