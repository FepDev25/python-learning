# repository_contract.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")
ID = TypeVar("ID", int, str)

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def find_all(self) -> List[T]:
        """Return all entities."""
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, entity_id: ID) -> Optional[T]:
        """Return entity by id or None."""
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def save(self, entity: T) -> T:
        """
        Insert if entity has no id; otherwise update.
        Returns the persisted entity.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity_id: ID) -> bool:
        """Delete by id. Returns True if deleted, False if not found."""
        raise NotImplementedError