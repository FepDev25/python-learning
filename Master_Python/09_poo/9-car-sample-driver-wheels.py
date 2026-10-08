from andres.poo.car.color import Color
from andres.poo.car.car import Car
from andres.poo.car.car_type import CarType
from andres.poo.car.engine import Engine, EngineType
from andres.poo.car.fuel_tank import FuelTank
from andres.poo.car.person import Person
from andres.poo.car.wheel import Wheel

mazda = Car.basic('Mazda', '3')
mazda.car_type = CarType.HATCHBACK
mazda.driver = Person('Luci', 'Martinez')
mazda.wheels = [Wheel('Yokohama', 16, 7.5) for _ in range(5)]
# print(mazda)

citroen = Car.with_color('Citroen', 'C3', Color.GRAY)
citroen.car_type = CarType.HATCHBACK
citroen.driver = Person('Pato', 'Lopez')

for i in range(5):
    citroen.add_wheel(Wheel('Michelin', 18, 10.5))
# print(citroen)

subaru_legacy = Car.with_cylinder('Subaru', 'Legacy', Color.RED, Engine(1.80, EngineType.DIESEL))
subaru_legacy.car_type = CarType.STATION_WAGON
subaru_legacy.driver = Person('Andres', 'Guzman')
for i in range(5):
    subaru_legacy.add_wheel(Wheel('Pirelli', 18, 10))
# print(subaru_legacy)

mazda_bt50 = Car.full_spec('Mazda', 'BT-50', Color.WHITE, Engine(3.00, EngineType.DIESEL), FuelTank(50))
mazda_bt50.car_type = CarType.PICKUP
mazda_bt50.driver = Person('Bea', 'Doe')
for i in range(5):
    mazda_bt50.add_wheel(Wheel('Pirelli', 21, 12))
# print(mazda_bt50)

subaru_impreza = Car.only_tank('Subaru', 'Impreza', FuelTank(50))
subaru_impreza.car_type = CarType.SEDAN
subaru_impreza.driver = Person('Lalo', 'Mena')
for i in range(5):
    subaru_impreza.add_wheel(Wheel('Yokohama', 18, 10))
# print(subaru_impreza)

nissan = Car.full_spec('Nissan', 'Navara', Color.PURPLE, Engine(2.5, EngineType.DIESEL), FuelTank(50))
nissan.car_type = CarType.PICKUP
nissan.driver = Person('Maria', 'Roe')

(nissan.add_wheel(Wheel('Michelin', 21, 12))
 .add_wheel(Wheel('Michelin', 21, 12))
 .add_wheel(Wheel('Michelin', 21, 12))
 .add_wheel(Wheel('Michelin', 21, 12))
 .add_wheel(Wheel('Michelin', 21, 12)))

# print(nissan)

suzuki = Car('Suzuki', 'Gran Vitara')
suzuki.color = Color.RED
suzuki.engine = Engine(1.8, EngineType.GASOLINE)
suzuki.fuel_tank = FuelTank()
suzuki.driver = Person('John', 'Doe')
suzuki.car_type = CarType.SUV

audi = Car()
audi.manufacturer = 'Audi'
audi.model = 'A5'
audi.car_type = CarType.SEDAN
audi.driver = Person('Jano', 'Perez')

cars = [mazda, citroen, subaru_legacy, mazda_bt50, subaru_impreza, nissan, suzuki, audi]
sorted_cars = sorted(cars)
for car in sorted_cars:
    print(car)


