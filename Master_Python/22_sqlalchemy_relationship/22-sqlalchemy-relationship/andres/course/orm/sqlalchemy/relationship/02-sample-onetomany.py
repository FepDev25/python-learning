from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer

Base.metadata.create_all(engine)

with SessionLocal() as session:
    customer1 = Customer(name="Pepe Joe", email="pepe@example.com")

    # Crear direcciones asociadas a ese cliente
    addr1 = Address(street="Calle Otra 1234", city="Santiago")
    addr2 = Address(street="Av. One Street 12", city="Santiago")

    # asociarlas al cliente
    customer1.addresses = [addr1, addr2]

    session.add(customer1)
    session.commit()

    # Consultar cliente y acceder a sus direcciones
    c = session.get(Customer, customer1.id)

    print("Cliente:", c.name)
    for a in c.addresses:
        print(" -", a.street, "-", a.city)

