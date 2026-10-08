from sqlalchemy import (
    Column, Integer, String
)
from sqlalchemy.orm import relationship

from andres.course.orm.sqlalchemy.relationship.config.db import Base
from andres.course.orm.sqlalchemy.relationship.models.student_course import student_course


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    # Relación unidireccional: desde Student podemos ver sus Courses
    courses = relationship(
        "Course",
        secondary=student_course,
        lazy="selectin", # carga eficiente de la colección
        back_populates='students'# Nota: no hay back_populates ni backref para mantenerlo unidireccional
    )

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"
