from course.sample.oop.abstractclass.validator.validator import Validator

class RequiredValidator(Validator):
    def __init__(self):
        super().__init__('El campo %s es requerido')

    def is_valid(self, value: str | None) -> bool:
        return value is not None and len(value) > 0