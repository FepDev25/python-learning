from course.andres.designpattern.observer.investor.corporation import Corporation
from course.andres.designpattern.observer.investor.investor import Investor

if __name__ == "__main__":
    # Creamos las corporaciones (sujetos)
    google_stock = Corporation("GOOGL", 2800.00)
    apple_stock = Corporation("AAPL", 150.00)

    # Creamos a los inversionistas (observadores)
    investor1 = Investor("Ana")
    investor2 = Investor("Carlos")
    investor3 = Investor("Sofía")

    # Los inversionistas se suscriben a las notificaciones de las corporaciones
    google_stock.attach(investor1)
    google_stock.attach(investor2)

    apple_stock.attach(investor2)
    apple_stock.attach(investor3)

    # Simulamos cambios de precios
    google_stock.price = 2825.50
    apple_stock.price = 155.75

    # Un inversionista decide dejar de seguir una acción
    print("\nCarlos ya no quiere seguir a Google.")
    google_stock.detach(investor2)

    # Otro cambio de precio
    google_stock.price = 2810.20