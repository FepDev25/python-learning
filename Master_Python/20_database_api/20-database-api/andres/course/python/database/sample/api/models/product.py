# models.py
from dataclasses import dataclass
from datetime import datetime

from andres.course.python.database.sample.api.models.category import Category


@dataclass
class Product:
    id: int | None
    name: str
    price: float
    created_at: datetime
    category: Category