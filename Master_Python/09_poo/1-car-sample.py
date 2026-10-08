from andres.poo.car.car import Car
from andres.poo.car.engine import Engine, EngineType
from andres.poo.car.fuel_tank import FuelTank

car = Car('Subaru')
car.set_color('Gris')
car.set_model('Impreza')
car.engine = Engine(1.5, EngineType.GASOLINE)
car.model = 'Impreza Modificado'
car.fuel_tank = FuelTank(30)
print(car.get_color())
print(car.details())
print(car.engine.cylinder)
print(car.accelerate_and_brake(4000, 120))


mazda = Car('Mazda', '3', 'Blanco', Engine(2.0, EngineType.GASOLINE))
mazda.engine.cylinder = 3.0
print(mazda.details())
print(mazda.engine.cylinder)
print(car)
print(repr(car))

print(mazda.accelerate(3000, 100))
print(mazda.brake())
print(f'Kilometros por litros: {mazda.calculate_consumption(300, 60)}')
print(f'Kilometros por litros: {mazda.calculate_consumption(300, 0.60)}')
