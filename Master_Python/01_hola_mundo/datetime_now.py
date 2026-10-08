import locale
from datetime import datetime

now = datetime.now()
print(f'La fecha actual es {now}')

date_time = datetime(2019, 4, 17, 14, 55, 59)
print(date_time)
print(date_time.year)
print(date_time.day)
print(date_time.month)
print(date_time.hour)
print(date_time.minute)
print(date_time.second)
print(date_time.microsecond)

date_format = date_time.strftime('%d/%m/%Y %H:%M') # %d/%m/%Y %I:%M %p formato 24 horas
print(date_format)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') # Spanish_Spain.1252
date_format = date_time.strftime('%d de %B, %Y')
print(date_format)