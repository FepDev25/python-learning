from course.andres.designpattern.observer.api.observable import Observable


class Corporation(Observable):
    """
    El Sujeto Concreto es dueño de algún estado importante y notifica a los
    observadores cuando el estado cambia.
    """
    def __init__(self, symbol: str, price: float):
        super().__init__()
        self._symbol = symbol
        self._price = price

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        El setter del precio permite cambiar el valor y notificar a los inversionistas.
        """
        print(f"\n[{self._symbol}] ¡Cambio de precio! Nuevo precio: ${new_price:.2f}")
        self._price = new_price
        self.notify('ejemplo de enviar algo al inversionista')