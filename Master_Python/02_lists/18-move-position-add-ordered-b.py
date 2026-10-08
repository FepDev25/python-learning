
numbers = [0] * 7

for i in range(len(numbers)):
    numbers[i] = int(input('Ingrese un numero: '))

element = int(input('Nuevo elemento: '))

position = next((i for i in range(len(numbers) - 1) if element <= numbers[i]), len(numbers) - 1)
last = numbers[-1]

for i in range(len(numbers) - 2, position - 1, -1):
    numbers[i + 1] = numbers[i]

new_list = numbers[:] + [0]

if element > last:
   new_list[-1] = element
else:
    new_list[-1] = last
    new_list[position] = element

print(numbers)
print(new_list)