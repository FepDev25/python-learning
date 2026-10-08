from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.course import Course
from andres.course.orm.sqlalchemy.relationship.models.student import Student
from andres.course.orm.sqlalchemy.relationship.models.student_course import student_course

Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        c_a = session.get(Course, 4)
        c_b = session.get(Course, 5)

        s_1 = session.get(Student, 3)
        s_2 = session.get(Student, 4)

        s_1.courses.append(c_a)
        s_1.courses.append(c_b)
        s_2.courses.append(c_b)

        session.commit()

        # Consultar: Student -> Courses (funciona)
        st = session.get(Student, s_1.id)
        print(f"Estudiante: {st.name}")
        for course in st.courses:
            print(" - cursa:", course.code, "-", course.title)

    except SQLAlchemyError as e:
        session.rollback()
        print(e)