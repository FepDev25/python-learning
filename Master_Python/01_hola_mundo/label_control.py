
for number in range(10):
    if number == 5:
       continue
    print(number)

users = ['Andrea', 'Pedro', 'Anonimo', 'Marta', 'Diego']

for user in users:
    if user == 'Anonimo':
        print('Usuario restringido.')
        continue
    print(f'Bienvendio, {user}')