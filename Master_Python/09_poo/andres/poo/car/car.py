from codecs import replace_errors
from typing import Final, Optional, List
from car_type import CarType
from color import Color
from engine import Engine
from fuel_tank import FuelTank
from person import Person
from wheel import Wheel


class Car:
    __license_plate_color = 'Orange'
    last_id: int = 0
    MAX_SPEED_HIGHWAY: Final[int] = 180
    COLOR_RED: Final[str] = 'Rojo'
    COLOR_WHITE: Final[str] = 'Blanco'
    COLOR_GRAY: Final[str] = "Gris Plata"
    COLOR_BLUE: Final[str] = 'Azul'
    COLOR_BLACK: Final[str] = 'Negro'
    COLOR_PURPLE: Final[str] = 'Morado'

    def __init__(self, manufacturer : str | None = None,
                 model : str | None = None,
                 color : str | Color | None = None,
                 engine : Optional[Engine] = None,
                 fuel_tank : Optional[FuelTank] = None):
        Car.last_id += 1
        self.__id: int = Car.last_id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__engine: Optional[Engine] = engine
        self.__fuel_tank: FuelTank | None = fuel_tank
        self.__car_type: Optional[CarType] = None
        self.__driver: Person|None = None
        self.__wheels: List[Wheel] = []

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, value):
        self.__engine = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def fuel_tank(self):
        if self.__fuel_tank is None:
            self.__fuel_tank = FuelTank()
        return self.__fuel_tank

    @fuel_tank.setter
    def fuel_tank(self, value):
        self.__fuel_tank = value

    @property
    def car_type(self):
        return self.__car_type

    @car_type.setter
    def car_type(self, value):
        self.__car_type = value

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        self.__manufacturer = value

    @property
    def driver(self) -> Person | None:
        return self.__driver

    @driver.setter
    def driver(self, value: Person):
        self.__driver = value

    @property
    def wheels(self) -> List[Wheel] | None:
        return self.__wheels

    @wheels.setter
    def wheels(self, value: List[Wheel]):
        self.__wheels = value

    @classmethod
    def empty(cls):
        return cls()

    @classmethod
    def basic(cls, manufacturer: str, model: str | Color):
        return cls(manufacturer, model)

    @classmethod
    def with_color(cls, manufacturer: str, model: str, color: str | Color):
        return cls(manufacturer, model, color)

    @classmethod
    def only_color(cls, manufacturer: str, color: str | Color):
        return cls(manufacturer, None, color)

    @classmethod
    def with_cylinder(cls, manufacturer: str, model: str, color: str | Color, engine: Optional[Engine]):
        return cls(manufacturer, model, color, engine)

    @classmethod
    def full_spec(cls, manufacturer: str, model: str, color: str | Color, engine: Optional[Engine], fuel_tank: Optional[FuelTank]):
        return cls(manufacturer, model, color, engine, fuel_tank)

    @classmethod
    def only_tank(cls, manufacturer: str, model: str, fuel_tank: Optional[FuelTank]):
        return cls(manufacturer, model, None, None, fuel_tank)

    @classmethod
    def set_license_plate_color(cls, value):
        cls.__license_plate_color = value

    @classmethod
    def get_license_plate_color(cls):
        return cls.__license_plate_color

    def set_model(self, value):
        self.__model = value

    def get_model(self):
        return self.__model

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

    def add_wheel(self, wheel: Wheel) -> 'Car':
        self.__wheels.append(wheel)
        return self

    def details(self):
        detail = f'manufacturer = {self.__manufacturer}\n'
        detail += f'model = {self.__model}\n'
        detail += f'color = {self.__color}\n'
        detail += f'engine = {self.__engine.cylinder if isinstance(self.__engine, Engine) else ''}\n\n'
        detail += f'patente = {Car.__license_plate_color}'
        detail += f'id = {self.__id}'
        return detail

    def accelerate(self, rpm, speed):
        return f'El auto {self.__manufacturer} acelerando a {rpm}rpm y a {speed}km/h'

    def brake(self):
        return f'{self.__manufacturer} {self.__model} frenando!'

    def accelerate_and_brake(self, rpm, speed):
        accelerating = self.accelerate(rpm, speed)
        braking = self.brake()
        return f'{accelerating}\n{braking}'

    def calculate_consumption(self, km, fuel_percentage):
        if isinstance(fuel_percentage, int):
            fuel_percentage = fuel_percentage/100.00
        return km/(fuel_percentage * self.fuel_tank.capacity)

    def __str__(self):
        return (f'Car(id={self.__id}, '
                f'manufacturer={self.__manufacturer}, '
                f'model={self.__model}, '
                f'color={self.__color.value if isinstance(self.__color, Color) else self.__color}, '
                f'tank={self.fuel_tank.capacity}, '
                f'cylinder: {self.__engine.cylinder if isinstance(self.__engine, Engine) else ''}, '
                f' license_plate_color={Car.__license_plate_color.value if isinstance(Car.__license_plate_color, Color) else Car.__license_plate_color}, '
                f'car_type={self.__car_type}, '
                f'car_type.name={self.__car_type.name if isinstance(self.__car_type, CarType) else self.__car_type}, '
                f'car_type.name_default={self.__car_type.name_default if isinstance(self.__car_type, CarType) else self.__car_type}, '
                f'car_type.description={self.__car_type.description if isinstance(self.__car_type, CarType) else self.__car_type}, '
                f'car_type.door_count={self.__car_type.door_count if isinstance(self.__car_type, CarType) else self.__car_type}), '
                f'driver={self.__driver}, '
                f'wheels={", ".join(str(w) for w in self.__wheels)}')

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Car):
            return False
        return self.__model == other.__model and self.__manufacturer == other.__manufacturer

    def __lt__(self, other: 'Car') -> bool:
        return self.__manufacturer < other.__manufacturer