from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person


# Crear nueva persona
with SessionLocal() as session:
    try:
        person = Person()
        person.name = 'Lalo'
        person.lastname = 'Doe'
        person.email = 'lalo@correo.com'
        person.age = 20
        session.add(person)
        session.commit()
        print(person)

    except SQLAlchemyError as e:
        session.rollback()
        print(e)
