from sqlalchemy import select

from andres.course.orm.sqlalchemy.config.db import Base, engine, SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
Base.metadata.create_all(engine)

# Listar todas las personas
with SessionLocal() as session:
    stmt = select(Person)
    people = session.scalars(stmt).all()
    for person in people:
        print(person)