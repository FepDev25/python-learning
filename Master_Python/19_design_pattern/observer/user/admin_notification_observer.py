from course.andres.designpattern.observer.api.observer import Observer
from course.andres.designpattern.observer.user.user_repository import UserRepository


class AdminNotificationObserver(Observer):
    def update(self, subject: UserRepository, user: dict) -> None:
        email = user.get("email")
        print(f"-> [Email al Admin]: Notificando al administrador que un nuevo usuario se ha registrado con el email: {email}.")
