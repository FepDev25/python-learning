from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Observer(ABC):
    """
    La interfaz del Observador declara el método de actualización, utilizado por los sujetos.
    """
    @abstractmethod
    def update(self, subject: 'Subject', obj: Optional[object]) -> None:
        """
        Recibe la actualización del sujeto.
        """
        pass