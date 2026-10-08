from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from andres.course.orm.sqlalchemy.mapped.person import Person
from andres.course.orm.sqlalchemy.repositories.repository import Repository

class PersonRepository(Repository[Person, int]):
    def __init__(self, session_factory):
        self._session_factory = session_factory

    def _session(self) -> Session:
        return self._session_factory()

    def find_all(self) -> List[Person]:
        with self._session() as session:
            return list(session.scalars(select(Person)).all())

    def find_by_id(self, entity_id: int) -> Optional[Person]:
        with self._session() as session:
            return session.get(Person, entity_id)

    def save(self, entity: Person) -> Person:
        with self._session() as session:
            try:
                # UPDATE si trae id válido
                if entity.id is not None and entity.id > 0:
                    current = session.get(Person, entity.id)
                    if not current:
                        raise ValueError(f"Person id={entity.id} no existe para actualizar.")
                    # copiar campos (evita problemas de objetos detach)
                    current.name = entity.name
                    current.lastname = entity.lastname
                    current.email = entity.email
                    current.age = entity.age
                    session.commit()
                    session.refresh(current)
                    return current
                # INSERT si no tiene id
                session.add(entity)
                session.commit()
                session.refresh(entity)
                return entity
            except SQLAlchemyError as e:
                session.rollback()
                raise
            except Exception:
                session.rollback()
                raise

    def remove(self, entity_id: int) -> bool:
        with self._session() as session:
            try:
                obj = session.get(Person, entity_id)
                if not obj:
                    return False
                session.delete(obj)
                session.commit()
                return True
            except SQLAlchemyError:
                session.rollback()
                raise
