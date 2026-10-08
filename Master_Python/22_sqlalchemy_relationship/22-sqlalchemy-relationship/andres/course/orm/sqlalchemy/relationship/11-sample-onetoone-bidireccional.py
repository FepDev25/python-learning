from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.medical_record import MedicalRecord
from andres.course.orm.sqlalchemy.relationship.models.patient import Patient

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        # Crear paciente y su registro médico
        p1 = Patient(name="Josefa Gonzalez", age=35)
        record = MedicalRecord(diagnosis="Gripe fuerte", treatment="Reposo e hidratación 2 semanas")
        p1.medical_record = record  # se asocia bidireccionalmente

        session.add(p1)
        session.commit()

        # Consultar desde Patient -> MedicalRecord
        patient = session.query(Patient).first()
        print(f"Paciente: {patient.name}, diagnóstico: {patient.medical_record.diagnosis}")

        # Consultar desde MedicalRecord -> Patient
        record = session.query(MedicalRecord).first()
        print(f"Registro médico #{record.id} pertenece a: {record.patient.name}")
    except SQLAlchemyError as e:
        session.rollback()
        print(e)