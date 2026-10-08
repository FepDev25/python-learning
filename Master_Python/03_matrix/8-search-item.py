
matrix = [
    [35, 90, 3, 1980],
    [15, 2020, 10, 5],
    [1990, 128, 32767, 1999],
    [2025, 127, 15, 2000]
]

search_item = 1980
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == search_item:
            found = True
            break
    if found:
        break

if found:
    print(f'Encontrado {search_item} en las cordenadas [{i},{j}]')
else:
    print(f'{search_item} no se encontro en la matriz')