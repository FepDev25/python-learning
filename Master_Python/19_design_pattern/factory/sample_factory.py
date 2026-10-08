from course.andres.designpattern.factory.factories.pizzeria_california_factory import PizzeriaCaliforniaFactory
from course.andres.designpattern.factory.factories.pizzeria_new_york_factory import PizzeriaNewYorkFactory
from course.andres.designpattern.factory.products.pizza_product import PizzaProduct

ny = PizzeriaNewYorkFactory()
california = PizzeriaCaliforniaFactory()

pizza: PizzaProduct = california.order_pizza("cheese")
print(f'Buce ordena la pizza {pizza.name}')

pizza = ny.order_pizza('pepperoni')
print('Andres ordena una', pizza.name)

pizza = california.order_pizza('vegetarian')
print(f'Jame ordena su pizza {pizza.name}')

pizza = ny.order_pizza('vegetarian')
print(f'Pepe ordena la pizza {pizza.name}')

pizza = ny.order_pizza('italian')
print('Linus ordena la pizza', pizza.name)