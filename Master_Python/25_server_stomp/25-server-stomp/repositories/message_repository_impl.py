from config.db import SessionLocal
from models.message import Message
from repositories.message_repository import MessageRepository
from sqlalchemy import select, desc, asc
from sqlalchemy.orm import Session
from typing import List

# ----------------------------
# Repositorio (implementación)
# ----------------------------
# ============================================================
# Implementación moderna usando select()
# ============================================================
class MessageRepositoryImpl(MessageRepository):

    def find_all(self) -> List["Message"]:
        """
        Devuelve todos los mensajes (solo type='MESSAGE'),
        ordenados cronológicamente (más antiguos primero).
        """
        with SessionLocal() as db:
            stmt = (
                select(Message)
                .where(Message.type == "MESSAGE")
                .order_by(asc(Message.date), asc(Message.id))
            )
            result = db.execute(stmt)
            return list(result.scalars().all())

    def save(self, message: "Message") -> "Message":
        """
        Inserta o actualiza un mensaje.
        """
        with SessionLocal() as db:
            db.add(message)
            db.commit()
            db.refresh(message)
            return message

    def get_last_messages(self, limit: int = 50) -> List["Message"]:
        with SessionLocal() as db:
            stmt = (
                select(Message)
                .where(Message.type == "MESSAGE")
                .order_by(desc(Message.id))
                .limit(limit)
            )
            result = db.execute(stmt)
            return list(reversed(result.scalars().all()))

    def get_last_messages_temp(self, limit: int = 50) -> List["Message"]:
        """
        Obtiene los últimos N mensajes (type='MESSAGE'),
        ordenados ascendentemente por fecha.
        """
        # Subconsulta con los últimos N mensajes (orden descendente)
        with SessionLocal() as db:
            subq = (
                select(Message)
                .where(Message.type == "MESSAGE")
                .order_by(desc(Message.date), desc(Message.id))
                .limit(limit)
                .subquery()
            )

            # Luego se reordena ascendentemente para mostrar en orden cronológico
            stmt = (
                select(Message)
                .join(subq, Message.id == subq.c.id)
                .order_by(asc(subq.c.date), asc(subq.c.id))
            )
            result = db.execute(stmt)
            return result.scalars().all()