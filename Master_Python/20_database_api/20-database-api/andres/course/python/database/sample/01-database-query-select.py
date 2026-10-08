from datetime import datetime

from andres.course.python.database.sample.api.database_connection import DatabaseConnection
from andres.course.python.database.sample.api.models.product import Product
from andres.course.python.database.sample.api.repositories.product_repository_impl import ProductRepositoryImpl

if __name__ == "__main__":

    repo = ProductRepositoryImpl()

    result = repo.find_all()

    print("Lista de productos:")
    for product in result:
        print(f"ID: {product.id}, Nombre: {product.name}, Precio: {product.price}, Creado en: {product.created_at}")

    print("\n=== Buscar por ID ===")
    product = repo.find_by_id(1)
    if product:
        print(product)
    else:
        print("Producto no encontrado")

    # 1. Crear un nuevo producto
    new_product = Product(
        id=None,
        name="Hamburguesa Palta tomate",
        price=4500.0,
        created_at=datetime.now()
    )

    saved_product = repo.save(new_product)
    print("Producto creado:", saved_product)

    # 2. Editar el producto recién creado
    saved_product.name = "Hamburguesa Premium Otro"
    saved_product.price = 8500.0

    updated_product = repo.save(saved_product)
    print("Producto actualizado:", updated_product)

    # 3. Consultar por ID
    product = repo.find_by_id(updated_product.id)
    print("Consulta por ID:", product)

    # Crear producto
    product = Product(id=None, name="Bebida Cola", price=1200.0, created_at=datetime.now())
    saved = repo.save(product)
    print("Creado:", saved)

    # Eliminar producto por ID
    deleted = repo.remove(saved.id)
    if deleted:
        print(f"Producto con id={saved.id} eliminado correctamente")
    else:
        print("No se encontró el producto a eliminar")

    # Verificar
    result = repo.find_by_id(saved.id)
    print("Consulta después del remove:", result)

    result = repo.find_all()

    print("Lista de productos:")
    for product in result:
        print(f"ID: {product.id}, Nombre: {product.name}, Precio: {product.price}, Creado en: {product.created_at}")

    conn = DatabaseConnection()
    conn.close_connection()