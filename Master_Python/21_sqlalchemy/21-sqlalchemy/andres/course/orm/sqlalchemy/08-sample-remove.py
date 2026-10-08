from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Eliminar persona
with SessionLocal() as session:
    try:
        person_removed = session.get(Person, 4)
        session.delete(person_removed)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
