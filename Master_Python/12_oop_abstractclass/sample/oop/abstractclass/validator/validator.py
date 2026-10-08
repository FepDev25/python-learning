from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, message: str):
        self._message = message

    @property
    def message(self):
        return self._message

    @abstractmethod
    def is_valid(self, value: str | None) -> bool:
        ...