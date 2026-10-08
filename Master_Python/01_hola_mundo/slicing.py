text = 'Andres Guzman'

print(text[0:6])
print(text[7:])
print(text[:6])
print(text[::])
print(text[::-1])
print(text[::3])

text = 'Python'
print(text[0:4])
print(text[:4])
print(text[2:])
print(text[::3])

text = "Hola Mundo"
new_text = text[:5] + text[5:].replace('Mundo', 'Python')
print(new_text)

text = 'Python es genial'
parts = text.split()
parts2 = parts[:2]
print(parts)
print(parts2)
parts_reverse = parts[::-1]
print(parts_reverse)
text_reverse = ' '.join(parts_reverse)
print(text_reverse)

text = 'Python'
print(text[:2].lower() + text[2:].upper())

text = '   Hola Python  '
print(text.strip()[:5])
print(text.strip()[5:])
