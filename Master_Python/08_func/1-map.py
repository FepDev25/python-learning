
numbers = [1, 2, 3, 4, 5, 6, 7]

numbers_x2 = list(map(lambda x: str(x * 2), numbers))
print(numbers_x2)

pairs_numbers = [str(x * 2) for x in numbers]
print(pairs_numbers)

names = ['Andres Guzman', 'Maria Perez', 'John Doe', 'Josefa Mena']
lastnames = list(map(lambda name: name.split()[1], names))
print(lastnames)
print(lastnames[1])
print(numbers)
print(names)