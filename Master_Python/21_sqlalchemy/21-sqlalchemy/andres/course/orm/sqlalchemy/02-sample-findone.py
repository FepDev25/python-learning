from sqlalchemy import select

from andres.course.orm.sqlalchemy.config.db import Base, engine, SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
Base.metadata.create_all(engine)

# Obtener una persona
with SessionLocal() as session:
    stmt = select(Person).where(Person.id == 1)
    person = session.scalar(stmt)
    print(person)

    stmt = select(Person).where(Person.id == 1)
    person2 = session.scalars(stmt).first()
    print(person)

    stmt = select(Person).where(Person.id == 1)
    person3 = session.execute(stmt).scalar_one()
    print(person)
    print(person == person2)
    print(person is person2)
    print(person2 == person3)
    print(person2 is person3)
    print(person == person2 == person3)
    print(person is person2 is person3)