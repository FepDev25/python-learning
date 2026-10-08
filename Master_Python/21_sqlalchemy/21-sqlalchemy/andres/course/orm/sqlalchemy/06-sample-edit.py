from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person


# Editar persona
with SessionLocal() as session:
    try:
        person_edit = session.get(Person, 4)

        if not person_edit:
            raise ValueError(f'Person id 4 no existe en la bbdd!')

        person_edit.name = 'Pepito'
        person_edit.email = 'pepito@correo.com'

        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
