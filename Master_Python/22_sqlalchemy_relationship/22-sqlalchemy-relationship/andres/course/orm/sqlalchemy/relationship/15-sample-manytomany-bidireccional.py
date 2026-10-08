from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.course import Course
from andres.course.orm.sqlalchemy.relationship.models.student import Student
from andres.course.orm.sqlalchemy.relationship.models.student_course import student_course

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        # Crear cursos
        c_spring = Course(code="CS-Spring", title="Spring desde cero")
        c_django = Course(code="CS-DJ", title="Django web Avanzado")
        c_nosql = Course(code="CS-NOSQL", title="Mongo DB")

        # Crear estudiantes
        s_julia = Student(name="Julia", email="julia@example.com")
        s_ale = Student(name="Alejandra", email="ale@example.com")

        # Asociaciones bidireccionales
        s_julia.courses = [c_spring, c_django]
        s_ale.courses = [c_django, c_nosql]

        # Al agregar por un lado, el otro se actualiza automáticamente
        session.add_all([s_julia, s_ale])
        session.commit()

        # Consultar desde Student → Courses
        student = session.query(Student).filter_by(name="Andrés Guzmán").first()
        print(f"Estudiante: {student.name}")
        for c in student.courses:
            print(" - cursa:", c.title)

        # Consultar desde Course → Students
        course = session.query(Course).filter_by(code="CS-PY").first()
        print(f"\nCurso: {course.title}")
        for s in course.students:
            print(" - alumno:", s.name)
    except SQLAlchemyError as e:
        session.rollback()
        print(e)