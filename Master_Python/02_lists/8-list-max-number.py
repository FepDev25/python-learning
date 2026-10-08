
a = []
print("Ingrese 5 enteros: ")
for i in range(5):
    num = int(input(f'Valor {i + 1}: '))
    a.append(num)
print(a)

max_index = 0

for i in range(1, len(a)):
    max_index = max_index if a[max_index] > a[i] else i

print(f'max = {a[max_index]}')