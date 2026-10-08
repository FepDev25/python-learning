from abc import ABC, abstractmethod

# Interfaz
class Formattable(ABC):
    @abstractmethod
    def format(self) -> str:
        pass


# Clase base concreta
class Text(Formattable):
    def __init__(self, content: str):
        self.content = content

    def format(self) -> str:
        return self.content


# Clase abstracta Decorador
class TextDecorator(Formattable, ABC):
    def __init__(self, text: Formattable):
        self._text = text


# Decoradores concretos
class UppercaseDecorator(TextDecorator):
    def format(self) -> str:
        return self._text.format().upper()


class ReverseDecorator(TextDecorator):
    def format(self) -> str:
        return self._text.format()[::-1]


class ReplaceSpacesDecorator(TextDecorator):
    def format(self) -> str:
        return self._text.format().replace(" ", "_")


class UnderlineDecorator(TextDecorator):
    def format(self) -> str:
        base = self._text.format()
        return f"{base}\n{'-' * len(base)}"


# Uso del patrón
if __name__ == "__main__":
    text = Text("Hola que tal Andres!")

    # uppercase = UppercaseDecorator(text)
    # reverse = ReverseDecorator(uppercase)
    # underline = UnderlineDecorator(reverse)
    # replace = ReplaceSpacesDecorator(underline)
    # print(replace.format())
    # Aplicamos decoradores en cadena
    decorated = UnderlineDecorator(
        ReplaceSpacesDecorator(
            ReverseDecorator(
                UppercaseDecorator(text)
            )
        )
    )
    print(decorated.format())

