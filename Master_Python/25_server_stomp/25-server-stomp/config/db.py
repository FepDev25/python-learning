import os

from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import (
    declarative_base, sessionmaker
)

# -*- coding: utf-8 -*-
"""
SQLAlchemy + MySQL (mysql-connector-python) para persistir el historial del chat.

Instalación:
  pip install SQLAlchemy mysql-connector-python

Configurar conexión:
  - Por defecto usa: mysql+mysqlconnector://chat:chat@localhost:3306/chatdb
  - Puedes sobrescribir con la variable de entorno DB_URL

Esquema:
  Tabla messages:
    - id (PK, autoincrement)
    - username (varchar(100), not null)
    - text (text, not null)
    - date (datetime, not null)
    - type (varchar(20), not null)
    - color (varchar(20), null)
    - created_at (datetime, not null, default now)
"""

# ----------------------------
# Configuración de conexión
# ----------------------------
DEFAULT_DB_URL = "mysql+mysqlconnector://root:sasa1234@localhost:3306/chatdb?charset=utf8mb4"
DB_URL = os.getenv("DB_URL", DEFAULT_DB_URL)

engine = create_engine(
    DB_URL,
    pool_pre_ping=True,
    pool_recycle=1800,   # 30 min
    future=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()







