from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer

Base.metadata.create_all(engine)

with SessionLocal() as session:
    customer1 = session.get(Customer, 1)

    # Crear direcciones asociadas a ese cliente
    addr1 = Address(street="Calle Principal 12345", city="Madrid")
    addr2 = Address(street="Av. Colon Street 123", city="Barcelona")

    # asociarlas al cliente
    customer1.addresses.append(addr1)
    customer1.addresses.append(addr2)

    session.commit()

    # Consultar cliente y acceder a sus direcciones
    c = customer1

    print("Cliente:", c.name)
    for a in c.addresses:
        print(" -", a.street, "-", a.city)

    session.delete(addr2)

    session.commit()

    print("Cliente:", c.name)
    for a in c.addresses:
        print(" -", a.street, "-", a.city)