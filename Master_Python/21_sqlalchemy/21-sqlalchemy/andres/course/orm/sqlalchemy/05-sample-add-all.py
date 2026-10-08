from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Guardar e insertar varias personas
with SessionLocal() as session:
    try:
        persons = [Person(name='Bruce', lastname='Roe', email='bruce@correo.com', age=50),
                   Person(name='Pepa', lastname='Gonzalez', email='pepa@correo.com', age=25)]

        session.add_all(persons)
        session.commit()
        print(persons)

    except SQLAlchemyError as e:
        session.rollback()
        print(e)
