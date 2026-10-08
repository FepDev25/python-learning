
def bubble_sort(list_array):
    total_element = len(list_array)
    count = 0

    for i in range(total_element - 1):
        for j in range(total_element - i - 1):
            if list_array[j + 1].__lt__(list_array[j]):
                list_array[j], list_array[j + 1] = list_array[j + 1], list_array[j]
            count += 1

    print(f'Contador: {count}')