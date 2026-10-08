from andres.poo.car.color import Color
from andres.poo.constants import Constants
from andres.poo.car.car import Car
from andres.poo.car.car_type import CarType
from andres.poo.car.engine import EngineType, Engine
from andres.poo.car.fuel_tank import FuelTank

Car.set_license_plate_color(Color.PURPLE)

car = Car.empty()
print(car)

car1 = Car.basic('Mazda', '3')
car1.car_type = CarType.HATCHBACK
print(car1)

car2 = Car.with_color('Citroen', 'C3', Color.GRAY)
car2.car_type = CarType.HATCHBACK
print(car2)

car3 = Car.with_cylinder('Subaru', 'Legacy', Color.RED, Engine(1.80, EngineType.DIESEL))
car3.car_type = CarType.STATION_WAGON
print(car3)

car4 = Car.full_spec('Mazda', 'BT-50', Color.WHITE, Engine(3.00, EngineType.DIESEL), FuelTank(50))
car4.car_type = CarType.PICKUP
print(car4)

car5 = Car.only_tank('Subaru', 'Impreza', FuelTank(50))
car5.car_type = CarType.SEDAN
print(car5)

car6 = Car.only_color('Subaru', Color.BLACK)
print(car6)
print(Car.get_license_plate_color().value)

speed_max_highway = Constants.MAX_SPEED_HIGHWAY
print(speed_max_highway)
print(Constants.MAX_SPEED_HIGHWAY)

for color in Color:
    print(color)
    print(color.name)
    print(color.value)

print(car1.car_type)
print(car1.car_type.name)
print(car1.car_type.name_default)
print(car1.car_type.description)
print(car1.car_type.door_count)
# Color.RED = 'rooojo'
# print(Color.RED)