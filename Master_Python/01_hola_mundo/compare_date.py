from datetime import date, datetime, timedelta

today = date.today()
birth = date(2025, 5, 5)
# str_birth = input('Ingrese una fecha (dd-mm-yyyy): ')
# birth = datetime.strptime(str_birth, '%d-%m-%Y').date()

if today == birth:
    print(f'Las fechas son iguales {today} y {birth}')
elif today > birth:
    print(f'La fecha de cumple {birth} es menor que hoy {today}')
else:
   print(f'La fecha de cumple {birth} es mayor que hoy {today}')

event = datetime(2025, 4, 17, 14, 0)
event2 = datetime(2025, 4, 25, 14, 2)

print(event < event2)
print(event > event2)
print(event == event2)

new_delta = event2 - event
print(new_delta)

new_date = event2 + timedelta(days=7, minutes=5, hours=2)
print(new_date)