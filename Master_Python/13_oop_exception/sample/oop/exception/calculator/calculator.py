from functools import singledispatchmethod

from andres.sample.oop.exception.calculator.division_by_zero_exception import DivisionByZeroException
from andres.sample.oop.exception.calculator.number_format_exception import NumberFormatException

class Calculator:

    @singledispatchmethod
    def divide(self, numerator, denominator):
        raise TypeError('Tipo no soportado')

    @divide.register
    def _(self, numerator: int, denominator: int) -> float:

        if denominator == 0:
            raise DivisionByZeroException('no se puede dividir por cero, es infinito!')

        return numerator / float(denominator)

    @divide.register
    def _(self, numerator: str, denominator: str) -> float:
        try:
            num = int(numerator)
            den = int(denominator)
            return self.divide(num, den)
        except ValueError:
            raise NumberFormatException('debe ingresar un numero en el numerador y divisor')