from dataclasses import dataclass
from typing import List

from course.andres.designpattern.observer.api.observable import Observable

@dataclass
class User:
    name: str
    email: str


class UserRepository(Observable):
    """
    El Sujeto Concreto contiene la lógica de negocio y notifica
    a los observadores cuando ocurre un evento importante.
    """

    def __init__(self):
        super().__init__()
        self._users: List[dict] = []

    def create_user(self, user_data: dict | User) -> dict:
        print("\nUserRepository: Creando un nuevo usuario...")

        if isinstance(user_data, User):
            user_data = {'name': user_data.name, 'email': user_data.email}

        self._users.append(user_data)

        # Notificar a todos los observadores sobre el nuevo usuario
        self.notify(user_data)

        return user_data