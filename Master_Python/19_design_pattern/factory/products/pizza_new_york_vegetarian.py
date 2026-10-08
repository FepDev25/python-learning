from typing import List
from dataclasses import dataclass, field

from course.andres.designpattern.factory.products.pizza_product import PizzaProduct

@dataclass
class PizzaNewYorkVegetarian(PizzaProduct):

    def __init__(self):
        super().__init__("Pizza vegetariana New York", "Masa integral vegana",
            "Salsa de tomate",
            ["Queso vegano", "Tomate", "Aceitunas", "Espinacas", "Berenjenas"]
        )

    def cook(self) -> None:
        print("Cocinando a 150 grados por 25 minutos")

    def cut(self) -> None:
        print("Cortando la pizza en rebanadas cuadradas")