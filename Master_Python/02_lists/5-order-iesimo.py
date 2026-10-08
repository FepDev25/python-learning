
numbers = [0] * 10
result = [0] * 10

for i in range(len(numbers)):
    numbers[i] = i + 1

index = 0
for i in range(len(numbers) // 2):
    result[index] = numbers[i]
    index += 1
    result[index] = numbers[len(numbers) - 1 - i]
    index += 1
    # print(f'{numbers[i]}: {numbers[len(numbers) - 1 - i]}')

for i in range(len(result)):
    print(f'i = {i} value: {result[i]}')