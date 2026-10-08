from andres.course.generics.truck.models.animal import Animal, AnimalType
from andres.course.generics.truck.models.car import Car
from andres.course.generics.truck.models.machinery import Machinery
from andres.course.generics.truck.models.truck import Truck

horses_transport: Truck[Animal] =  Truck(5)
horses_transport.add(Animal('Peregrino', AnimalType.CABALLO))
horses_transport.add(Animal('Grillo', AnimalType.CABALLO))
horses_transport.add(Animal('Topocalma', AnimalType.BOVINO))
horses_transport.add(Animal('Longotoma', AnimalType.CABALLO))

for item_animal in horses_transport:
    print(f'{item_animal.name} tipo: {item_animal.type.value}')

machines_transport: Truck[Machinery] = Truck(3)
machines_transport.add(Machinery('Bulldozer'))
machines_transport.add(Machinery('Grua Horquilla'))
machines_transport.add(Machinery('Perforadora'))

for item_machine in machines_transport:
    print(f'{item_machine.type}')

cars_transport: Truck[Car] = Truck(3)
cars_transport.add(Car('Toyota'))
cars_transport.add(Car('Mitsubishi'))
cars_transport.add(Car('Chevrolet'))

for item_car in cars_transport:
    print(item_car.brand)