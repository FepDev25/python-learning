from typing import List, Optional

import mysql.connector

from andres.course.python.database.sample.api.database_connection import DatabaseConnection
from andres.course.python.database.sample.api.models.category import Category
from andres.course.python.database.sample.api.models.product import Product
from andres.course.python.database.sample.api.repositories.product_repository import Repository


class ProductRepositoryImpl(Repository):

    def find_all(self) -> List[Product]:
        db = DatabaseConnection()  # Siempre devuelve la misma instancia
        connection = db.get_connection()
        products: List[Product] = []
        try:
            # Conexión a la base de datos (se cierra automáticamente al salir del bloque with)
            # with db.get_connection() as connection:

            # Crear cursor (también se cierra automáticamente)
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT p.id, p.name, p.price, p.created_at,
                   c.id AS category_id, c.name AS category_name
            FROM products p
            JOIN categories c ON c.id = p.category_id
            ORDER BY p.id
            """)
                for product_id, name, price, create_at, cid, cname in cursor.fetchall():
                    products.append(Product(product_id, name, price, create_at, Category(cid, cname)))

        except mysql.connector.Error as e:
            print("Error al conectar o consultar la base de datos:", e)

        return products

    def find_by_id(self, product_id: int) -> Optional[Product]:
        connection = DatabaseConnection().get_connection()

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT p.id, p.name, p.price, p.created_at,
                                   c.id AS category_id, c.name AS category_name
                            FROM products p
                            JOIN categories c ON c.id = p.category_id
                            WHERE p.id = %s
                        """
                ,
                (product_id,)
            )
            row = cursor.fetchone()

            if row:
                (pid, pname, price, created_at, cid, cname) = row
                return Product(
                    id=pid,
                    name=pname,
                    price=price,
                    created_at=created_at,
                    category=Category(id=cid, name=cname)
                )
        return None

    def save(self, product: Product) -> Product:
        connection = DatabaseConnection().get_connection()

        if product.id is not None and product.id > 0:
            # UPDATE
            sql = """
                UPDATE products
                SET name = %s, price = %s, category_id = %s
                WHERE id = %s
            """
            values = (product.name, product.price, product.category.id, product.id)
        else:
            # INSERT
            sql = """
                  INSERT INTO products (name, price, created_at, category_id)
                  VALUES (%s, %s, %s, %s)
                  """
            values = (product.name, product.price, product.created_at, product.category.id)

        with connection.cursor() as cursor:
            cursor.execute(sql, values)
            connection.commit()

            # Si es un insert, asignar el id generado al objeto
            if cursor.lastrowid:
                product.id = cursor.lastrowid

        return product

    def remove(self, product_id: int) -> bool:
        connection = DatabaseConnection().get_connection()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            connection.commit()
            return cursor.rowcount > 0  # True si borró algún registro

