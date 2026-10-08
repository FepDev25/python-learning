from dataclasses import dataclass

from course.andres.designpattern.factory.products.pizza_product import PizzaProduct

@dataclass
class PizzaNewYorkPepperoni(PizzaProduct):

    def __init__(self):
        super().__init__(
            _name="Pizza Pepperoni New York",
            _dough="Masa delgada a la piedra",
            _sauce="Salsa de tomate",
            _ingredients=["Queso mozzarella", "Extra pepperoni", "Aceitunas"]
        )

    def cook(self) -> None:
        print("Cocinando por 40 minutos a 90 grados C")

    def cut(self) -> None:
        print("Cortando la pizza en triángulos")