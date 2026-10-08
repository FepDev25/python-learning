from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer
from andres.course.orm.sqlalchemy.relationship.models.invoice import Invoice

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        # 1) Crear un cliente con facturas (añadiéndolas por el lado del Customer)
        c = session.get(Customer, 2)
        c.invoices = [Invoice(amount=340), Invoice(amount=570)]
        c.invoices.append(Invoice(amount=870))
        session.commit()

        # 2) Agregar otra factura asignándola por el lado de Invoice
        inv4 = Invoice(amount=700, customer=c)
        session.add(inv4)
        session.commit()

        # 3) Consultar desde Invoice -> Customer (many-to-one)
        inv = session.get(Invoice, inv4.id)
        print("Factura", inv.id, "de", inv.amount, "pertenece a:", inv.customer.name)

        # 4) Consultar desde Customer -> Invoices (one-to-many)
        print("Cliente:", c.name)
        for i in c.invoices:
            print(" - Invoice:", i.id, "monto:", i.amount)

        # 5) (Opcional) Eliminar una factura quitándola de la colección
        #    gracias a delete-orphan, al removerla de customer.invoices se elimina de la BBDD
        to_remove = c.invoices[-1]
        c.invoices.remove(to_remove)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)