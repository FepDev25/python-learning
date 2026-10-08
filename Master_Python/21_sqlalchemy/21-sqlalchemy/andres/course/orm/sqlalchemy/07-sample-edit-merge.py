from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Editar persona
with SessionLocal() as session:
    try:
        person_edit = Person(id=4, age=46)

        person_edit.name = 'Jose'
        person_edit.email = 'jose@correo.com'

        session.merge(person_edit)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
