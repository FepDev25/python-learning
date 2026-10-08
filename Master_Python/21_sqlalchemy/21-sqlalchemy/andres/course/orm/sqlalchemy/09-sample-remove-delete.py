from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.config.db import SessionLocal
from andres.course.orm.sqlalchemy.mapped.person import Person

# Eliminar persona
with SessionLocal() as session:
    try:
        stmt = delete(Person).where(Person.id == 5)
        session.execute(stmt)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(e)
