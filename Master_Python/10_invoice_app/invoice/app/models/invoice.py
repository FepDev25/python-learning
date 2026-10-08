from datetime import datetime
from typing import Optional, List

from invoice.app.models.customer import Customer
from invoice.app.models.item import Item


class Invoice:
    __last_folio = 0

    def __init__(self, description: str, customer: Optional[Customer]):
        Invoice.__last_folio += 1
        self.__folio_id = Invoice.__last_folio

        self.__date = datetime.now()
        self.__description = description
        self.__customer = customer

        self.__items: List[Item] = []

    @property
    def folio_id(self):
        return self.__folio_id

    @property
    def date(self):
        return self.__date

    @property
    def customer(self):
        return self.__customer

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    @property
    def description(self):
        return self.__description

    def add_item(self, item: Item) -> 'Invoice':
        self.__items.append(item)
        return self

    def calculate_total2(self):
        total = 0.00
        for item in self.items:
            total += item.calculate_amount()

        return total

    def calculate_total(self) -> float:
        return sum(float(item.calculate_amount()) for item in self.items)

    def generate_detail(self):
        detail = f'Factura Numero: {self.__folio_id}\n'

        detail += str(self.customer)
        detail += f'Descripción: {self.description}\n'
        detail += f'Fecha Emision: {self.date.strftime('%d de %B, %Y')}\n'

        detail += f'Nombre\t\t$\t\tCant.\t\tTotal\n'

        for item in self.items:
            detail += str(item)

        detail += f'\nGran Total: {self.calculate_total():.2f}'

        return detail

    def __str__(self):
        return self.generate_detail()

