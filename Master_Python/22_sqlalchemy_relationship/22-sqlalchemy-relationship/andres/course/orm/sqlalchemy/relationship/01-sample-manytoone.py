from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer
from andres.course.orm.sqlalchemy.relationship.models.invoice import Invoice

Base.metadata.create_all(engine)

with SessionLocal() as session:
    # Crear un cliente
    customer1 = Customer(name="Andrés Guzmán", email="andres@example.com")
    session.add(customer1)
    session.commit()

    # Crear facturas asociadas a ese cliente
    invoice1 = Invoice(amount=100, customer=customer1)
    invoice2 = Invoice(amount=250, customer=customer1)

    session.add_all([invoice1, invoice2])
    session.commit()

    # Consultar facturas y acceder al cliente desde cada una
    invoices = session.query(Invoice).all()
    for inv in invoices:
        print(inv.id, inv.amount, "-> Cliente:", inv.customer.name)