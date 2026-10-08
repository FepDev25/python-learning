# user_repository.py
from __future__ import annotations
from typing import List, Optional, Callable

from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from course.andres.tkinter.db.crud.models.user import User
from course.andres.tkinter.db.crud.repositories.repository import Repository

# <- tu modelo User
class UserRepository(Repository[User, int]):

    def __init__(self, session: Session):
        self._session = session

    def find_all(self) -> List[User]:
        return list(self._session.execute(select(User)).scalars().all())

    def find_by_id(self, entity_id: int) -> Optional[User]:
        session = self._session
        return session.get(User, entity_id)

    def search(self, query: str) -> list[User]:
        """
        Busca por name, username o email usando LIKE case-insensitive.
        Devuelve lista ordenada por id DESC.
        """
        q = (query or "").strip()
        if not q:
            return self.find_all()

        pattern = f"%{q}%"
        stmt = (
            select(User)
            .where(
                or_(
                    User.name.ilike(pattern),
                    User.username.ilike(pattern),
                    User.email.ilike(pattern),
                )
            )
            .order_by(User.id.desc())
        )
        return list(self._session.execute(stmt).scalars().all())

    def save(self, entity: User) -> User:
        """
        - INSERT: si entity.id es None -> add + commit + refresh
        - UPDATE: si entity.id tiene valor -> carga existente, copia campos, commit
        """
        session = self._session
        try:
            if getattr(entity, "id", None) is None:
                session.add(entity)
                session.commit()
                session.refresh(entity)
                return entity
            else:
                existing = session.get(User, entity.id)
                if not existing:
                    # O bien podrías decidir hacer upsert; aquí lanzamos error claro
                    raise ValueError(f"User with id={entity.id} not found for update")

                # Copiamos campos actualizables
                existing.name = entity.name
                existing.username = entity.username
                existing.email = entity.email
                existing.password = entity.password

                session.commit()
                session.refresh(existing)
                return existing
        except Exception:
            session.rollback()
            raise

    def remove(self, entity_id: int) -> bool:
        session = self._session
        try:
            obj = session.get(User, entity_id)
            if not obj:
                return False
            session.delete(obj)
            session.commit()
            return True
        except Exception:
            session.rollback()
            raise