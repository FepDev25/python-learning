from typing import Optional

from course.sample.oop.inheritance.models.person import Person


class Student(Person):

    def __init__(self, first_name: str | None = None,
                 last_name: Optional[str] = None,
                 email: Optional[str] = None,
                 institution: str | None = None,
                 math_grade: float = 0.00,
                 language_grade: float = 0.00,
                 history_grade: float = 0.00):
        super().__init__(first_name, last_name, email)
        self.institution = institution
        self.math_grade = math_grade
        self.language_grade = language_grade
        self.history_grade = history_grade

    def greet(self):
        return f"{super().greet()} soy {self.first_name} un estudiante y estudio en {self.institution}"

    def speak(self):
        return 'El alumno hace una pregunta al profesor!'

    def write_blackboard(self):
        return 'El alumno desarrolla un tema en la pizarra'

    def calculate_average(self) -> float:
        return (self.math_grade + self.language_grade + self.history_grade)/3

    def __str__(self):
        return (super().__str__() +
                f'\ninstitucion={self.institution}, '
                f'nota matematica={self.math_grade}, '
                f'nota lenguaje={self.language_grade},'
                f'nota de historia={self.history_grade}, '
                f'promedio={self.calculate_average()}')
