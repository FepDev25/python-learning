
person = dict(mather_last_name='Doe', account=12345, bank='Banco el ....')
person['name'] = 'Andres'
person['name'] = 'Pepe'
person['last_name'] = 'Guzman'
person.update({'age': 30, 'email': 'andres@correo.com'})

address = {
    'country': 'USA',
    'state': 'California',
    'city': 'Los Angeles',
    'street': "One Street",
    "number": "1234"
}
person['address'] = address

print('persona = ', person)

first_name = person.get('name')
last_name = person['last_name']

print(first_name, last_name)

name_bank = person.pop('bank')
# del person['bank']
print(person)
print(f'valor eliminado es {name_bank}')

other = person.get('other')
# other = person['other']
print(f'Un valor que no existe: {other}')

print(len(person))
print('contiene elementos: ', len(person)>0, bool(person))
print(person.keys())
print(person.values())
print(person.items())

has_key = 'last_name' in person
print(f'boolean = {has_key}')

has_values = 'andres@correo.com' in person.values()
print(f'existe = {has_values}')

for value in person.values():
    print(f'value: {value}')

for key in person.keys():
    print(f'k: {key}')

for key, value in person.items():
    print(key, '=>', value)

address_person = person.get('address', {})
country = address_person.get('country')
city = address_person['city']
postal_code = address_person.get('postal_code', '342314')
print(f'El pais de {first_name} es {country}')
print(f'La ciudad de {first_name} es {city}')
print(f'El codigo postal de {first_name} es {postal_code}')

for key in person.keys():
    value = person.get(key)
    if isinstance(value, dict):
        if 'address' in person:
            country = value.get('country')
            state = value.get('state')
            city = value.get('city')
            print(f'{key} => La direccion de {person.get('name')} es { country } {state} {city}')
    else:
        print(f'{key} => {value}')


for key, value in person.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(sub_key, '=>', sub_value)
    else:
        print(f'{key} => {value}')
