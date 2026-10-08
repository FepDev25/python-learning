from typing import List

from abc import ABC, abstractmethod
from sqlalchemy.orm import (Session)
from models.message import Message

# ----------------------------
# Repositorio (contrato)
# ----------------------------
class MessageRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Message]:
        pass

    @abstractmethod
    def save(self, message: Message) -> Message:
        pass

    @abstractmethod
    def get_last_messages(self, limit: int = 50) -> List[Message]:
        pass