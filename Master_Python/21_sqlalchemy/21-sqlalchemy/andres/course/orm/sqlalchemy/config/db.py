# Configuración de la base de datos SQLite (puede ser cualquier motor)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+mysqlconnector://root:sasa1234@localhost:3306/python_course", echo=True,
                        pool_size=10,
                       max_overflow=20,
                       pool_timeout=30,
                       pool_recycle=1800)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()