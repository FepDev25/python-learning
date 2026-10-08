from dataclasses import dataclass

from course.andres.designpattern.factory.products.pizza_product import PizzaProduct

@dataclass
class PizzaNewYorkItalian(PizzaProduct):

    def __init__(self):
        super().__init__(
            _name="Pizza Italiana New York",
            _dough="Masa gruesa",
            _sauce="Salsa de tomate italiano con carne",
            _ingredients=["Queso mozzarella", "Aceitunas", "Jamón", "Choricillo", "Champiñones"]
        )

    def cook(self) -> None:
        print("Cocinando por 10 minutos a 200 grados")

    def cut(self) -> None:
        print("Cortando la pizza en pequeños triángulos")