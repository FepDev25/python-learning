from course.andres.designpattern.observer.api.observer import Observer
from course.andres.designpattern.observer.user.user_repository import UserRepository


class LogRecordObserver(Observer):
    def update(self, subject: UserRepository, user: dict) -> None:
        name = user.get("name")
        print(f"-> [Log]: Guardando registro en el log. Nuevo usuario: '{name}' registrado.")
