from typing import Iterable, TypeVar

from customer import Customer

T = TypeVar('T', Customer, int)
def from_array_to_list(items: Iterable[T]) -> list[T]:
    return list(items)

customers: set[Customer] = {Customer('Andres', 'Doe')}
customers.add(Customer('John', 'Roe'))
customers.add(Customer('John', 'Roe'))

numbers: set[int] = {1,2,3,4,5}

customers_list = from_array_to_list(customers)

numbers_list = from_array_to_list(numbers)

for c in customers_list:
    print(c)

for n in numbers_list:
    print(n)