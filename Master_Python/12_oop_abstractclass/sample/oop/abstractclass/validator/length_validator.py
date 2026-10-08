import sys

from course.sample.oop.abstractclass.validator.validator import Validator


class LengthValidator(Validator):
    def __init__(self, min_len: int = 0, max_len: int = sys.maxsize):
        super().__init__('el campo %s debe tener un minimo %d y un maximo %d caracteres')
        self._min: int = min_len
        self._max: int = max_len

    def is_valid(self, value: str | None) -> bool:
        self._message = self._message % ('%s', self._min, self._max)

        if value is None:
            return True

        return self._min <= len(value) <= self._max