from andres.poo.car.car import Car
from andres.poo.car.engine import EngineType, Engine
from andres.poo.car.fuel_tank import FuelTank

Car.set_license_plate_color(Car.COLOR_PURPLE)

car = Car.empty()
print(car)

car1 = Car.basic('Mazda', '3')
print(car1)

car2 = Car.with_color('Citroen', 'C3', Car.COLOR_GRAY)
print(car2)

car3 = Car.with_cylinder('Subaru', 'Legacy', Car.COLOR_RED, Engine(1.80, EngineType.DIESEL))
print(car3)

car4 = Car.full_spec('Mazda', 'BT-50', Car.COLOR_WHITE, Engine(3.00, EngineType.DIESEL), FuelTank(50))
print(car4)

car5 = Car.only_tank('Subaru', 'Impreza', FuelTank(50))
print(car5)

car6 = Car.only_color('Subaru', Car.COLOR_BLACK)
print(car6)
print(Car.get_license_plate_color())

speed_max_highway = Car.MAX_SPEED_HIGHWAY
print(speed_max_highway)
print(Car.MAX_SPEED_HIGHWAY)
