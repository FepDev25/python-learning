from course.andres.designpattern.factory.factories.pizzeria_zone_abstract_factory import PizzeriaZoneAbstractFactory
from course.andres.designpattern.factory.products.pizza_california_cheese import PizzaCaliforniaCheese
from course.andres.designpattern.factory.products.pizza_california_vegerarian import PizzaCaliforniaVegetarian


class PizzeriaCaliforniaFactory(PizzeriaZoneAbstractFactory):

    def create_pizza(self, pizza_type: str):
        match pizza_type.lower():
            case "cheese":
                return PizzaCaliforniaCheese()
            case "vegetarian":
                return PizzaCaliforniaVegetarian()
            case _:
                return None