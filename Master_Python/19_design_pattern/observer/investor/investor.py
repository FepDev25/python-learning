from course.andres.designpattern.observer.api.observer import Observer
from course.andres.designpattern.observer.investor.corporation import Corporation

class Investor(Observer):
    """
    Los Observadores Concretos reaccionan a las actualizaciones emitidas por el Sujeto
    al que han sido suscritos.
    """

    def __init__(self, name: str):
        self._name = name

    def update(self, subject: Corporation, obj: object | None) -> None:
        notification = f"> Notificación para {self._name}: El precio de '{subject.symbol}' ha cambiado a ${subject.price:.2f} con data adicional {obj}"
        print(notification)