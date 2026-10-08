
tuple_number = (10, 20, 30, 40, 50, 20)

tuple_number2 = 1, 2, 3, 4, 5

tuple_number3 = (50,)
is_integer = (50)

colors = 'rojo', 'verde', 'amarillo'
colors2 = ('rojo', 'azul', 'amarillo', 'naranja', 'verde', 'azul')

print(colors2[-1]) # verde
print(colors[0]) # rojo
print(colors[2]) # amarillo

for color in colors2:
    print(f'color = {color}')

print(colors2.count('azul'))
print(colors2.index('naranja'))
print(tuple_number.count(20))
print(tuple_number.index(30))

position = {('x', 'y'): 3.1415}
position2 = {('x', 'y', 'z'): 7.1415}

print(position[('x', 'y')])
print(position2[('x', 'y', 'z')])
