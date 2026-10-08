from invoice.app.models.product import Product


class Item:

    def __init__(self, quantity, product: Product | None):
        self.__quantity = quantity
        self.__product = product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        self.__product = value

    def calculate_amount(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{str(self.product)}\t\t{self.quantity}\t\t{self.calculate_amount():.2f}\n'