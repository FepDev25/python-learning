from dataclasses import dataclass
from threading import Condition

@dataclass
class Bakery:
    bread: str = ''
    available: bool = False

    def __post_init__(self):
        self.condition = Condition()

    def bake(self, dough: str):
        with self.condition:
            while self.available:
                self.condition.wait()
            self.bread = dough
            print(f'Panadero hornea: {self.bread}')
            self.available = True
            self.condition.notify()

    def consume(self):
        with self.condition:
            while not self.available:
                self.condition.wait()
            print(f'Cliente consume: {self.bread}')
            self.available = False
            self.condition.notify()