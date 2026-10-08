
mi_set = {'Pera', 'Manzana'}
mi_set.add('Sandia')
print(mi_set)

mi_set.update(['Naranja', 'Limon', 'Mandarina'])
print(mi_set)

mi_set.update({'Maracuya', 'Mango'})
print(mi_set)

mi_set |= {'Platano', 'Durazno', 'Damasco'}
print(mi_set)

new_fruits = {'Melon', 'Palta'}
for fruit in new_fruits:
    mi_set.add(fruit)

mi_list_ordered = sorted(mi_set)
print(mi_list_ordered)