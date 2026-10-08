from dataclasses import dataclass, field
from typing import List, Iterable, Iterator, TypeVar, Generic

from andres.course.generics.truck.models.animal import Animal
from andres.course.generics.truck.models.car import Car
from andres.course.generics.truck.models.machinery import Machinery

T = TypeVar('T', Animal, Machinery, Car)
@dataclass
class Truck(Generic[T], Iterable[T]):

    capacity: int
    # __items: List[T] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self):
        self.__items: List[T] = []

    def add(self, item: T) -> 'Truck':
        if len(self.__items) >= self.capacity:
             raise ValueError('Capacidad del camion excedida!')
        else:
             self.__items.append(item)
        return self

    def __iter__(self) -> Iterator[T]:
        return iter(self.__items)

    def __len__(self) -> int:
        return len(self.__items)
