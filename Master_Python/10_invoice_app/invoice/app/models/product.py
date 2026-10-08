class Product:

    def __init__(self, name: str, price: float):
        self.__name: str = name
        self.__price: float = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return f'{self.name}\t\t{self.price:.2f}'