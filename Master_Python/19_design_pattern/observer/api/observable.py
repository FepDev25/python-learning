from typing import List, Optional

from course.andres.designpattern.observer.api.observer import Observer
from course.andres.designpattern.observer.api.subject import Subject

class Observable(Subject):
    """
    El Sujeto Concreto es dueño de algún estado importante y notifica a los
    observadores cuando el estado cambia.
    """
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"Agregado un nuevo observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, obj: Optional[object] = None) -> None:
        """
        Dispara una notificación a cada observador.
        """
        print(f"Notificando a los observadores...")
        for observer in self._observers:
            observer.update(self, obj)