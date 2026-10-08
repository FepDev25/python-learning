from dataclasses import dataclass

from course.andres.designpattern.factory.products.pizza_product import PizzaProduct


@dataclass
class PizzaCaliforniaCheese(PizzaProduct):

    def __init__(self):
        super().__init__(
            _name="Pizza California Queso",
            _dough="Masa a la piedra delgada",
            _sauce="Salsa de tomate con rúcula",
            _ingredients=["Extra queso mozzarella", "Cebolla", "Queso azul"]
        )

    def cook(self) -> None:
        print("Cocinando a 35 minutos a 100 grados")

    def cut(self) -> None:
        print("Cortando la pizza en pequeños triángulos")