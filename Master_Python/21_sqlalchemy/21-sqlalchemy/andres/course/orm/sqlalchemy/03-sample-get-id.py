from andres.course.orm.sqlalchemy.config.db import Base, engine, SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Crear las tablas si no existen
Base.metadata.create_all(engine)

# Obtener por id
with SessionLocal() as session:
    person = session.get(Person, 1)
    person2 = session.get(Person, 2)
    person3 = session.get(Person, 3)
    person4 = session.get(Person, 2)
    print(person)
    print(person2)
    print(person3)
    print(person4)
    print(person4 is person2)
    print(person4 == person2)
