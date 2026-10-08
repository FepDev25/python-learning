
import calendar
from datetime import datetime

current_date = datetime.now()
print(f'Fecha actual: {current_date}')

days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
day_index = current_date.weekday()
week_day_name = days[day_index]
print(f'Hoy es {week_day_name}')

if calendar.isleap(current_date.year):
    print(f'{current_date.year} es un año bisiesto')
else:
    print(f'{current_date} no es bisiesto')

print('Calendario del mes actual')
print(calendar.month(current_date.year, current_date.month))

first_weekday, days_in_month = calendar.monthrange(current_date.year, current_date.month)
print(days[first_weekday])
print(days_in_month)

modified_date = current_date.replace(year=2024, month=12, day=25, hour=7, minute=45, second=30)
print(f'Fecha modificada: {modified_date}')


if calendar.isleap(modified_date.year):
    print(f'{modified_date.year} es un año bisiesto')
else:
    print(f'{modified_date} no es bisiesto')

print('Calendario del mes actual')
print(calendar.month(modified_date.year, modified_date.month))

first_weekday, days_in_month = calendar.monthrange(modified_date.year, modified_date.month)
print(days[first_weekday])
print(days_in_month)