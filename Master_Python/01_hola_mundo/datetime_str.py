import locale
from datetime import datetime

text = '17/04/2025 18:30'
date_time = datetime.strptime(text, '%d/%m/%Y %H:%M')
print(date_time)
print(date_time.year)
print(date_time.month)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # windows -> Spanish_Spain.1252
date_str = '17 abril, 2025'
format = '%d %B, %Y'
date_obj = datetime.strptime(date_str, format)
print(date_obj)

date_str = "17 de abr, 2025 23:30"
format = '%d de %b, %Y %H:%M'
date_obj = datetime.strptime(date_str, format)
print(date_obj)

try:
    date_str = '17/04/2025 02:30 PM'
    format = '%d/%m/%Y %I:%M %p'
    date_obj = datetime.strptime(date_str, format)
    print(date_obj)
    print(datetime.strftime(date_obj, '%d de %B, %Y, %I:%M%p'))
except ValueError as err:
    print("Error en el formato de fecha: ", err)