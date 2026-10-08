from course.sample.oop.abstractclass.validator.validator import Validator

class NotNoneValidator(Validator):
    def __init__(self):
        super().__init__('El campo %s no puede ser nulo')

    def is_valid(self, value: str | None) -> bool:
        return value is not None