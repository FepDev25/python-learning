from course.andres.designpattern.observer.api.observer import Observer
from course.andres.designpattern.observer.user.user_repository import UserRepository

class WelcomeEmailObserver(Observer):
    def update(self, subject: UserRepository, user: dict) -> None:
        name = user.get("name")
        email = user.get("email")
        print(f"-> [Email al Usuario]: Enviando email de bienvenida a {name} a la dirección {email}.")
