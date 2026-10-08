
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

@dataclass
class PizzaProduct(ABC):
    _name: str
    _dough: str
    _sauce: str
    _ingredients: List[str] = field(default_factory=list)

    def prepare(self) -> None:
        print(f"Preparando la pizza '{self._name}' con masa '{self._dough}' "
              f"y salsa '{self._sauce}'. Ingredientes: {', '.join(self._ingredients) or 'ninguno'}")

    @abstractmethod
    def cook(self) -> None:
        pass

    @abstractmethod
    def cut(self) -> None:
        pass

    def pack(self) -> None:
        print(f"Empacando la pizza '{self._name}' en su caja oficial.")

    @property
    def name(self) -> str:
        return self._name