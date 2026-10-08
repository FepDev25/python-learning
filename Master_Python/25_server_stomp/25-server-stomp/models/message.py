# ----------------------------
# Modelo ORM
# ----------------------------
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    String, Text, DateTime, func, BigInteger
)
from sqlalchemy.orm import (
    Mapped, mapped_column
)
from config.db import Base, engine


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(BigInteger().with_variant(BigInteger, "mysql"), primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    text: Mapped[str] = mapped_column(Text, nullable=False, default="")
    date: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, index=True)
    type: Mapped[str] = mapped_column(String(20), nullable=False, index=True, default="MESSAGE")
    color: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self) -> str:
        return f"<Message id={self.id} @{self.username} type={self.type} date={self.date.isoformat() if self.date else None}>"


# Crear tablas si no existen
Base.metadata.create_all(engine)