from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Subject(ABC):
    """
    La interfaz del Sujeto declara un conjunto de métodos para gestionar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        """
        Agrega un observador al sujeto.
        """
        pass

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        """
        Elimina un observador del sujeto.
        """
        pass

    @abstractmethod
    def notify(self, obj: Optional[object] = None) -> None:
        """
        Notifica a todos los observadores sobre un evento.
        """
        pass