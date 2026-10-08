from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint

from andres.course.orm.sqlalchemy.relationship.config.db import Base

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
    # (opcional) reforzar unicidad explícita
    UniqueConstraint("student_id", "course_id", name="uq_student_course")
)