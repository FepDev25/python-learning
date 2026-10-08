from course.sample.oop.abstractclass.validator.validator import Validator

class NumberValidator(Validator):

    def __init__(self):
        super().__init__('el campo %s debe ser un numero')

    def is_valid(self, value: str | None) -> bool:
        if value is None:
            return False

        try:
            int(value)
            return True
        except (ValueError, TypeError):
            return False
