
fish = ['Corvina', 'Lenguado', 'Pejerrey', 'Robalo', 'Atun', 'Palometa', 'Robalo']
print(fish)

unique = set()
duplicates = set()
for f in fish:
    if f in unique:
        print('Elemento duplicado', f)
        duplicates.add(f)
    else:
        unique.add(f)

# unique.difference_update(duplicates)
unique -= duplicates

print(len(unique), 'elementos no duplicados:', unique)
print(len(duplicates), 'elementos duplicados', duplicates)