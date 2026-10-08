from dataclasses import dataclass
from enum import Enum

class AnimalType(Enum):
    CABALLO = 'Caballo'
    BURRO = 'Burro'
    NOVILLO = 'Novillo'
    BOVINO = 'Bovino'

@dataclass
class Animal:
    name: str
    type: AnimalType

