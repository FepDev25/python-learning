from andres.poo.car.color import Color
from andres.poo.car.car import Car
from andres.poo.car.car_type import CarType
from andres.poo.car.engine import Engine, EngineType
from andres.poo.car.fuel_tank import FuelTank

Car.set_license_plate_color(Color.PURPLE)

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

car_type = car5.car_type
match car_type:
    case CarType.CONVERTIBLE:
        print('El automovil es deportivo y descapotable de dos puertas')
    case CarType.COUPE:
        print('Es un automovil pequeño de dos puertas y tipicamente deportivo')
    case CarType.VAN:
        print('Es un automovil utilitario de transporte de empresas, de 3 puertas')
    case CarType.HATCHBACK:
        print('Es un automovil mediano compacto, aspecto deportivo')
    case CarType.SEDAN:
        print('Es un automovil mediano')
    case CarType.PICKUP:
        print('Es un automovil de doble cabina o camioneta')
    case CarType.STATION_WAGON:
        print('Es un automovil mas grande con maleta grande...')

for ct in CarType:
    print(f'{ct} => {ct.name}, {ct.name_default}, {ct.description}, {ct.door_count}')
