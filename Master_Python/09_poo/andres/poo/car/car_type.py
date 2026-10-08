from enum import Enum

class CarType(Enum):
    SEDAN = ('Sedan', 'Auto mediano', 4)
    STATION_WAGON = ('Station Wagon', 'Auto grande', 5)
    HATCHBACK = ('Hatchback', 'Auto Compacto', 5)
    PICKUP = ('Pickup', 'Camioneta', 4)
    COUPE = ('Coupe', 'Auto pequeño', 2)
    CONVERTIBLE = ('Convertible', 'Auto deportivo', 2)
    VAN = ('Furgon', 'Auto de transporte o utilitario', 3)
    SUV = ('SUV', 'Todo terren deportivo', 5)

    def __init__(self, name, description, door_count):
        self.__name = name
        self.__description = description
        self.__door_count = door_count

    @property
    def name_default(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def door_count(self):
        return self.__door_count

