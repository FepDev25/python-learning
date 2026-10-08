import locale
from functools import reduce

import numpy as np
import statistics
numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)

total2 = np.array(numbers).sum()
print(total2)

scores = (80, 90, 100)
average = statistics.mean(scores)
print(average)

words = ['apple', 'banana', 'pear', 'grape']
shortest = min(words, key=len)
print(shortest)

palabras = ['Manazana', 'Uva', 'Banana', 'arándanos']
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') # Spanish_Spain.1252
menor = min(palabras, key=locale.strxfrm)
print(menor)

mayor = max(palabras, key=str.lower)
mayor2 = max(palabras, key=len)
print(mayor)
print(mayor2)

max_int = max(numbers)
min_int = min(numbers)
print(max_int)
print(min_int)

people = [
    {'name': 'Ana', 'age': 28},
    {'name': 'Luis', 'age': 35},
    {'name': 'Carlos', 'age': 30}
]

oldest = max(people, key=lambda p: p['age'])
print(oldest['name'])

palabras = ['Zorro', 'abeja', 'Mono']
palabras_ordenadas = sorted(palabras, key=str.upper, reverse=True)
print(palabras_ordenadas)

a = sorted(people, key=lambda k: k['age'], reverse=True)
b = sorted(people, key=lambda i: i['name'])
c = sorted(people, key=lambda j: len(j['name']))
print(a)
print(b)
print(c)

d = sum(p['age'] for p in people)
print(d)

e = reduce(lambda initial, current: initial + current['age'], people, 0)
print(e)