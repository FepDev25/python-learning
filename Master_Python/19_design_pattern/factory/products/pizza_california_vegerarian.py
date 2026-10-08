from dataclasses import dataclass

from course.andres.designpattern.factory.products.pizza_product import PizzaProduct

@dataclass
class PizzaCaliforniaVegetarian(PizzaProduct):

    def __init__(self):
        super().__init__('', '', '')
        self._name = "Pizza California Vegetariana",
        self._dough = "Masa delgada Light",
        self._sauce = "Salsa BBQ Light",
        self._ingredients = ["Queso mozzarella", "Aceitunas", "Espinacas", "Cebolla", "Berenjenas", "Choclo"]

    def cook(self) -> None:
        print("Cocinando por 25 minutos a 180 grados")

    def cut(self) -> None:
        print("Cortando la pizza en rebanadas rectangulares")