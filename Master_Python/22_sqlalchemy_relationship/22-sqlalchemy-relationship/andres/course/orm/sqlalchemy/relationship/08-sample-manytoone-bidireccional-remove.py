from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer
from andres.course.orm.sqlalchemy.relationship.models.invoice import Invoice

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        c = session.get(Customer, 2)
        inv = session.get(Invoice, 7)
        c.invoices.remove(inv)
        session.commit()
        # 4) Consultar desde Customer -> Invoices (one-to-many)
        print("Cliente:", c.name)
        for i in c.invoices:
            print(" - Invoice:", i.id, "monto:", i.amount)

    except SQLAlchemyError as e:
        session.rollback()
        print(e)