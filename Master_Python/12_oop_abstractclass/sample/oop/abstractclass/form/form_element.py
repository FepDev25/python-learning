from abc import ABC, abstractmethod
from typing import List

from course.sample.oop.abstractclass.validator.validator import Validator


class FormElement(ABC):

    def __init__(self, name: str):
        self._name: str = name
        self._value: str | None = None
        self.__validators: List[Validator] = []
        self.__errors: List[str] = []

    def add_validator(self, validator: Validator):
        self.__validators.append(validator)

    @property
    def errors(self):
        return self.__errors

    def set_value(self, value: str):
        self._value = value

    def is_valid(self) -> bool:
        self.__errors.clear()
        for v in self.__validators:
            if not v.is_valid(self._value):
                self.__errors.append(v.message % self._name)
        return len(self.__errors) == 0


    @abstractmethod
    def draw_html(self) -> str:
        pass