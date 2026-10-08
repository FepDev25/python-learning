
text = 'Hola'
if text:
    print('Pasa porque el texto no esta vacio!')

text = ' '.strip()
if text:
    print('pasa el texto? o no pasa?')

persons = []
if persons:
    print('pasa pq tiene elementos la lista')

number = 0
if number:
    print('pasa el numero?')

if persons is not None:
    print('perfecto la lista contiene elementos!')

if text is not None:
    print('el texto no es none o null')
elif text:
    print('el texto no es vacio')
else:
    print('el texto es vacio')