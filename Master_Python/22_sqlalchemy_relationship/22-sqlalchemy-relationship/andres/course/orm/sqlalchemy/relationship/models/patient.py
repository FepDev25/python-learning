from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from andres.course.orm.sqlalchemy.relationship.config.db import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    # relación inversa: un paciente tiene un registro médico
    medical_record = relationship(
        "MedicalRecord",
        back_populates="patient",
        uselist=False,              # importante: indica relación uno a uno, no lista
        cascade="all, delete-orphan"  # opcional: elimina registro médico si se borra el paciente
    )

    def __repr__(self):
        return f"Patient(id={self.id}, name='{self.name}', age={self.age})"

