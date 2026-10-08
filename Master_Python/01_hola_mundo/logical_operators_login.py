
usernames = ['andres', 'admin', 'pepe', 'josefa']
passwords = ['1234', '12345', '123', 'abcde']

user = input('Ingrese el username: ')
password = input('Ingrese una clave: ')

authenticated = False

for i in range(len(usernames)):
    # print(i)
    authenticated = usernames[i] == user and passwords[i] == password
    if authenticated:
        break
    # if usernames[i] == user and passwords[i] == password:
    #     authenticated = True
    #     break

message = f'Bienvenido Usuario {user}, ha iniciado sesion con exito!' \
    if authenticated else \
    'Username o password incorrecto! \nLo sentimos, requiere autenticacion!'
print(f'message = {message}')

# if authenticated:
#     print(f'Bienvenido Usuario {user}, ha iniciado sesion con exito!')
# else:
#     print('Username o password incorrecto! \nLo sentimos, requiere autenticacion!')