from andres.poo.car.vehicle import Vehicle

car = Vehicle()
print(car)

car1 = Vehicle('Mazda', '3')
print(car1)

car2 = Vehicle('Citroen', 'C3', 'Gris')
print(car2)

car3 = Vehicle('Subaru', 'Legacy', 'Rojo', 1.80)
print(car3)

car4 = Vehicle('Mazda', 'BT-50', 'Blanco', 3.00, 50.00)
print(car4)

car5 = Vehicle('Subaru', 'Impreza', None, None, 50.00)
print(car5)

car6 = Vehicle('Subaru', None, 'Negro')
print(car6)

car7 = Vehicle(manufacturer='Nissan', color='Gris')
print(car7)

car8 = Vehicle(model='L200', cylinder=3.00)
print(car8)