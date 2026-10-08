from course.andres.designpattern.factory.factories.pizzeria_zone_abstract_factory import PizzeriaZoneAbstractFactory
from course.andres.designpattern.factory.products.pizza_new_york_italian import PizzaNewYorkItalian
from course.andres.designpattern.factory.products.pizza_new_york_pepperoni import PizzaNewYorkPepperoni
from course.andres.designpattern.factory.products.pizza_new_york_vegetarian import PizzaNewYorkVegetarian

class PizzeriaNewYorkFactory(PizzeriaZoneAbstractFactory):

    def create_pizza(self, pizza_type: str):
        match pizza_type.lower():
            case "vegetarian":
                return PizzaNewYorkVegetarian()
            case "pepperoni":
                return PizzaNewYorkPepperoni()
            case "italian":
                return PizzaNewYorkItalian()
            case _:
                return None