import math
import random

colors = ['azul', 'amarillo', 'rojo', 'verde', 'blanco', 'negro']
random_val = random.random()
random_val *= len(colors)
random_val = math.floor(random_val)
print(f'color: {colors[int(random_val)]}')
print('Numero aleatorio: ', random_val)

random_int = random.randint(15, 25)
print(random_int)

random_val = random.randint(0, len(colors) - 1)
print(colors[random_val])

random_range = random.randrange(len(colors))
print(colors[random_range])

random_range = random.randrange(2, 9, 3)
print(random_range)

random_value = random.uniform(15, 25)
print(random_value)