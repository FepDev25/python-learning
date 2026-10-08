from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer

Base.metadata.create_all(engine)

with SessionLocal() as session:
    addr4 = session.get(Address, 4)

    session.delete(addr4)

    session.commit()

    c = session.get(Customer, 4)
    print("Cliente:", c.name)
    for a in c.addresses:
        print(" -", a.street, "-", a.city)