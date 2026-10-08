from dataclasses import dataclass
from datetime import date

@dataclass
class OperationWithBalance:
    id: int
    company: str
    account_number: str
    issuer: str
    operation: str
    movement_date: date
    instrument: str
    quantity: float
    balance: float
    price: float