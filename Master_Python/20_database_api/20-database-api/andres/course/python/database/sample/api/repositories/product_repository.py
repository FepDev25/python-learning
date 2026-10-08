# repository.py
from abc import ABC, abstractmethod
from typing import List, Optional

import mysql.connector

from andres.course.python.database.sample.api.models.product import Product

class Repository(ABC):

    @abstractmethod
    def find_all(self) -> List[Product]:
        ...

    @abstractmethod
    def find_by_id(self, product_id: int) -> Optional[Product]:
        ...

    @abstractmethod
    def save(self, product: Product) -> Product:
        ...

    @abstractmethod
    def remove(self, product_id: int) -> bool:
        ...