from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer
from andres.course.orm.sqlalchemy.relationship.models.invoice import Invoice

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        # 1) Crear un cliente con facturas (añadiéndolas por el lado del Customer)
        c = Customer(name="John Doe", email="john.doe@example.com")
        c.invoices = [Invoice(amount=100), Invoice(amount=250)]
        session.add(c)
        session.commit()

        # 2) Agregar otra factura asignándola por el lado de Invoice
        inv3 = Invoice(amount=400, customer=c)
        session.add(inv3)
        session.commit()

        # 3) Consultar desde Invoice -> Customer (many-to-one)
        inv = session.get(Invoice, inv3.id)
        print("Factura", inv.id, "de", inv.amount, "pertenece a:", inv.customer.name)

        # 4) Consultar desde Customer -> Invoices (one-to-many)
        customer = session.get(Customer, c.id)
        print("Cliente:", customer.name)
        for i in customer.invoices:
            print(" - Invoice:", i.id, "monto:", i.amount)

        # 5) (Opcional) Eliminar una factura quitándola de la colección
        #    gracias a delete-orphan, al removerla de customer.invoices se elimina de la BBDD
        to_remove = customer.invoices[0]
        customer.invoices.remove(to_remove)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)