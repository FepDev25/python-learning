
name = 'Andres Guzman'
course = 'Curso de python'
name_upper = name.upper()
print(name == name_upper)
print(name_upper)
print(name)
print(course.lower())

words = 'curso de python'
print(words.capitalize())
print(words.title())

words = '    hola Andres   '
print(words.strip())
print(words.lstrip())
print(words.rstrip())

text = 'Hola Java'
new_text = text.replace('Java', 'Python')
print(text)
print(new_text)

text = 'Andres,Guzman,Python,Java,Angular'
data_list = text.split(',')
print(data_list[2])
print(data_list[4])
print(data_list)

data = ['Andres2', 'Guzman2', 'Python2', 'Java2', 'Angular2']
text = '/'.join(data)
print(text)

text = 'Hola, Andres que tal como estas!'
print(text.find('tal'))
print(text.index('como'))

print(text.startswith('Hola,'))
print(text.endswith('!'))

number = '1234'
decimal = '1234.45'
text = 'Python'
mix = 'Python3'

print(number.isnumeric())
print(number.isdigit())
print(decimal.isdecimal())
print(mix.isalnum())
print(mix.isalpha())
print(text.isalpha())

text = '   hola Andres como estas, bienvenido al curso de Python!     '
text_clean = text.strip().capitalize().title()
print(text_clean)

new_text = text_clean.replace('Curso De Python', 'Curso de Python 3')
print(new_text)

words = new_text.split()
print(words)