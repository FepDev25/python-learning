from datetime import datetime

from andres.course.python.database.sample.api.database_connection import DatabaseConnection
from andres.course.python.database.sample.api.models.category import Category
from andres.course.python.database.sample.api.models.product import Product
from andres.course.python.database.sample.api.repositories.product_repository_impl import ProductRepositoryImpl

if __name__ == "__main__":

    repo = ProductRepositoryImpl()

    result = repo.find_all()

    print("Lista de productos:")
    for product in result:
        print(f"ID: {product.id}, Nombre: {product.name}, "
              f"Precio: {product.price}, "
              f"Creado en: {product.created_at}, "
              f"Category: {product.category}")


    # Crear producto en categoría 2 (por ejemplo, "Comidas")
    p = Product(
        id=None,
        name="Hamburguesa Doble",
        price=7200.0,
        created_at=datetime.now(),
        category=Category(id=2, name="Comidas")  # name opcional para DTO; el INSERT usa id
    )
    p = repo.save(p)
    print("Creado:", p)

    # Cambiar nombre, precio y mover a categoría 3 (por ejemplo, "Promos")
    p.name = "Hamburguesa Doble Promo"
    p.price = 6800.0
    p.category = Category(id=3, name="Promos")
    p = repo.save(p)
    print("Actualizado:", p)

    # Consultar
    print("find_by_id:", repo.find_by_id(p.id))
    print("find_all:", repo.find_all()[:10])  # muestra primeros 3

    conn = DatabaseConnection()
    conn.close_connection()