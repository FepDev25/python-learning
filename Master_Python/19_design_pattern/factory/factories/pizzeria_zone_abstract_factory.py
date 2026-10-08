from abc import ABC, abstractmethod

from course.andres.designpattern.factory.products.pizza_product import PizzaProduct


class PizzeriaZoneAbstractFactory(ABC):

    def order_pizza(self, pizza_type: str)  -> PizzaProduct:
        pizza = self.create_pizza(pizza_type)
        print(f"------------ Fabricando la pizza {pizza.name} ------------")
        pizza.prepare()
        pizza.cook()
        pizza.cut()
        pizza.pack()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> PizzaProduct:
        pass