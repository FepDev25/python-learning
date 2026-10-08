import re

from course.sample.oop.abstractclass.validator.validator import Validator

class EmailValidator(Validator):
    EMAIL_REGEX = re.compile(r'^(.+)@(.+)$')
    def __init__(self):
        super().__init__('el campo %s tiene un formato de correo invalido')

    def is_valid(self, value: str | None) -> bool:
        if value is None:
            return False
        return bool(self.EMAIL_REGEX.match(value))