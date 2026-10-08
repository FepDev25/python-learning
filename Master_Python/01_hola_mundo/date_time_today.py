from datetime import date

today = date.today()
print(f'Hoy es {today}')
print(f'Year es {today.year}')
print(f'Month es {today.month}')
print(f'Day es {today.day}')

birthday = date(1990, 10, 7)
print(f'El cumpleaños es {birthday}')
