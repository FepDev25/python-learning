from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:

    MAX_SPEED_HIGHWAY: int = 180
    COLOR_RED: str = 'Rojo'
    COLOR_WHITE: str = 'Blanco'
    COLOR_GRAY: str = "Gris Plata"
    COLOR_BLUE: str = 'Azul'
    COLOR_BLACK: str = 'Negro'
    COLOR_PURPLE: str = 'Morado'