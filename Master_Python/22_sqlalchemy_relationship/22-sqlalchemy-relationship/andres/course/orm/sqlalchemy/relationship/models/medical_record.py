from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from andres.course.orm.sqlalchemy.relationship.config.db import Base


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True)
    diagnosis = Column(String(100))
    treatment = Column(String(100))
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True)  # UNIQUE para one-to-one

    # relación unidireccional: desde el registro accedemos al paciente
    patient = relationship("Patient", back_populates="medical_record")

    def __repr__(self):
        return f"MedicalRecord(id={self.id}, diagnosis='{self.diagnosis}', patient={self.patient})"
