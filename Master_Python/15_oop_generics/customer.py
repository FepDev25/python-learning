from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    lastname: str

    def __hash__(self):
        return hash((self.name, self.lastname))
