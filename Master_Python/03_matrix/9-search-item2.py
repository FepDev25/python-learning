
matrix = [
    [35, 90, 3, 1980],
    [15, 2020, 10, 5],
    [1990, 128, 32767, 1999],
    [2025, 127, 15, 2000]
]

search_item = 128
found = next(((i,j)
              for i, row in enumerate(matrix)
              for j, value in enumerate(row)
              if value == search_item),
             None)

if found:
    i, j = found
    print(f'Encontrado {search_item} en las cordenadas [{i},{j}]')
else:
    print(f'{search_item} no se encontro en la matriz')