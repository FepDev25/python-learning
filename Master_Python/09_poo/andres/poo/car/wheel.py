
class Wheel:

    def __init__(self, manufacturer: str, rim_size: int, width: float):
        self.manufacturer = manufacturer
        self.rim_size = rim_size
        self.width = width

    def __str__(self):
        return f'{self.manufacturer} - {self.rim_size}x{self.width}'