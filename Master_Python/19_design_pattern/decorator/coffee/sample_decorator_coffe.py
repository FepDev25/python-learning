from __future__ import annotations
from abc import ABC, abstractmethod


# === Interfaz / Componente ===
class Configurable(ABC):
    @abstractmethod
    def get_base_price(self) -> float: ...
    @abstractmethod
    def get_ingredients(self) -> str: ...


# === Componente concreto ===
class Coffee(Configurable):
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    def get_base_price(self) -> float:
        return self._price

    def get_ingredients(self) -> str:
        return self._name


# === Decorador base (abstracto) ===
class CoffeeDecorator(Configurable, ABC):
    def __init__(self, coffee: Configurable) -> None:
        self._coffee = coffee

    def get_base_price(self) -> float:
        # Delegación por defecto; los hijos añaden costo
        return self._coffee.get_base_price()

    def get_ingredients(self) -> str:
        # Delegación por defecto; los hijos añaden ingredientes
        return self._coffee.get_ingredients()


# === Decoradores concretos ===
class WithCramDecorator(CoffeeDecorator):
    """Añade 'crema' (mantengo el nombre que pediste)."""
    def get_base_price(self) -> float:
        return super().get_base_price() + 2.50

    def get_ingredients(self) -> str:
        return f"{super().get_ingredients()}, Crema"


class WithMilkDecorator(CoffeeDecorator):
    def get_base_price(self) -> float:
        return super().get_base_price() + 1.75

    def get_ingredients(self) -> str:
        return f"{super().get_ingredients()}, Leche"


class WithChocolataDecorator(CoffeeDecorator):
    """Añade 'chocolate' (mantengo el nombre que pediste)."""
    def get_base_price(self) -> float:
        return super().get_base_price() + 2.00

    def get_ingredients(self) -> str:
        return f"{super().get_ingredients()}, Chocolate"


# === Ejemplo de uso ===
if __name__ == "__main__":
    # Base espresso
    espresso = Coffee("Espresso", 3.00)

    # Café Mocha = Espresso + Leche + Chocolate
    cafe_mocha: Configurable = WithChocolataDecorator(WithMilkDecorator(espresso))

    # Cappuccino = Espresso + Leche + Crema
    cafe_capuchino: Configurable = WithCramDecorator(WithMilkDecorator(espresso))

    # Espresso solo
    cafe_espresso: Configurable = espresso

    # Mostrar resultados
    bebidas = [
        ("Café Mocha", cafe_mocha),
        ("Café Capuchino", cafe_capuchino),
        ("Café Espresso", cafe_espresso),
    ]

    for nombre, bebida in bebidas:
        print(f"{nombre}:")
        print(f"  Ingredientes: {bebida.get_ingredients()}")
        print(f"  Precio final: ${bebida.get_base_price():.2f}\n")