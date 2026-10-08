from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ajusta estos valores a tu entorno
DB_USER = "root"
DB_PASSWORD = "sasa1234"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "py_kardex"

DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    "?charset=utf8mb4"
)

# Engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=True,        # pon True si quieres ver el SQL en consola
    future=True
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

# Base para modelos ORM
Base = declarative_base()