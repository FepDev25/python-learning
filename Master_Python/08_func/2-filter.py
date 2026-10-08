
nums = [1, 2, 3, 4, 5, 6]

pairs = list(filter(lambda y: y % 2 == 0, nums))
print(pairs)

pairs2 = [y for y in nums if y % 2 == 0]
print(pairs2)

names = ['Andres Guzman', 'Pepe Doe', 'Mariela Gonzalez', 'Claudio Roe', 'James Gosling', 'Bruce Doe']
filter_names = list(filter(lambda name: name.split()[1] == 'Doe', names))
filter_names2 = [name for name in names if name.split()[1] == 'Doe']
print(filter_names2)
print(filter_names)

new_nums = list(filter(lambda x: x != 3, nums))
print(new_nums)

