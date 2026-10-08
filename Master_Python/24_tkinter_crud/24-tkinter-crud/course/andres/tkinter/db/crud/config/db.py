from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la conexión a MySQL
DATABASE_URL = "mysql+mysqlconnector://root:sasa1234@localhost:3306/db_crud_tkinter"

# Crear el engine
engine = create_engine(DATABASE_URL, echo=True, pool_size=50)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()