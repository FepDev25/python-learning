from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def find_all(self) -> List[T]:
        ...

    @abstractmethod
    def find_by_id(self, entity_id: ID) -> Optional[T]:
        ...

    @abstractmethod
    def save(self, entity: T) -> T:
        ...

    @abstractmethod
    def remove(self, entity_id: ID) -> bool:
        ...