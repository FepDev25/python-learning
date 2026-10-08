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
        c_java = Course(code="CS-JAVA", title="Java desde cero")
        c_py = Course(code="CS-PY", title="Python Avanzado")
        c_db = Course(code="CS-DB", title="Bases de Datos con SQL")
        session.add_all([c_java, c_py, c_db])

        # Crear estudiantes y asociar cursos desde el lado Student
        s_andres = Student(name="Andrés Guzmán", email="andres@example.com")
        s_maria = Student(name="María Pérez", email="maria@example.com")

        s_andres.courses = [c_java, c_py]
        s_maria.courses = [c_py, c_db]

        session.add_all([s_andres, s_maria])
        session.commit()

        # Consultar: Student -> Courses (funciona)
        st = session.get(Student, s_andres.id)
        print(f"Estudiante: {st.name}")
        for course in st.courses:
            print(" - cursa:", course.code, "-", course.title)

        # Remover una asociación (sin borrar el curso)
        st.courses.remove(c_java)
        session.commit()

        # Consultar estudiantes de un curso (NO hay relación inversa):
        # se hace con un JOIN manual
        course_to_inspect = c_py
        q = (
            select(Student)
            .join(student_course, Student.id == student_course.c.student_id)
            .where(student_course.c.course_id == course_to_inspect.id)
        )
        students_in_python = session.scalars(q).all()
        print(f"Alumnos en {course_to_inspect.title}: {[s.name for s in students_in_python]}")
    except SQLAlchemyError as e:
        session.rollback()
        print(e)