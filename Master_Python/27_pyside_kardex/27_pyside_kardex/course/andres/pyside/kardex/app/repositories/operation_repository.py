from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional
from course.andres.pyside.kardex.app.entity.operation import Operation
from course.andres.pyside.kardex.app.models.dto.operation_with_balance import OperationWithBalance


class OperationRepository(ABC):

    @abstractmethod
    def find_by_id(self, operation_id: int) -> Optional[Operation]:
        pass

    @abstractmethod
    def find_all(self, offset: int = 0, limit: int = 100) -> List[Operation]:
        pass

    @abstractmethod
    def find_all_with_balance(self, offset: int = 0, limit: int = 100) -> List[OperationWithBalance]:
        pass

    @abstractmethod
    def save(self, operation: Operation) -> Operation:
        pass

    @abstractmethod
    def delete(self, operation_id: int) -> bool:
        pass