from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer

Base.metadata.create_all(engine)

with SessionLocal() as session:
    customer_pepe = session.get(Customer, 4)
    addr7 = session.get(Address, 7)

    customer_pepe.addresses.remove(addr7)

    session.commit()

    c = session.get(Customer, 4)
    print("Cliente:", c.name)
    for a in c.addresses:
        print(" -", a.street, "-", a.city)