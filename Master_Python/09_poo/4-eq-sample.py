from datetime import date

from andres.poo.car.car import Car
from andres.poo.car.engine import Engine, EngineType
from andres.poo.car.fuel_tank import FuelTank

car = Car.full_spec('Mazda', 'BT-50', 'Blanco',  Engine(3.00, EngineType.DIESEL), FuelTank(50))
car2 = Car.full_spec('Mazda', 'BT-50', 'Blanco',  Engine(3.00, EngineType.DIESEL), FuelTank(50))
car3 = car
date_now = date.today()
print(car is car2)
print(car == car2)
