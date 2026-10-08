from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.medical_record import MedicalRecord
from andres.course.orm.sqlalchemy.relationship.models.patient import Patient

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        p2 = session.get(Patient, 2)

        # Crear su registro médico asociado
        record = MedicalRecord(diagnosis="Gripe común", treatment="Reposo e hidratación", patient=p2)
        session.add(record)
        session.commit()

        # Consultar el registro médico y acceder al paciente
        r = session.scalar(select(MedicalRecord).where(MedicalRecord.id == record.id))
        print(f"Registro #{r.id}: diagnóstico={r.diagnosis}, paciente={r.patient.name}")
    except SQLAlchemyError as e:
        session.rollback()
        print(e)