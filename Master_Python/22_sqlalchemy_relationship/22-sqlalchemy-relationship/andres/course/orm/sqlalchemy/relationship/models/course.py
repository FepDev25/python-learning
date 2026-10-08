from sqlalchemy import (
    Column, Integer, String
)
from sqlalchemy.orm import relationship

from andres.course.orm.sqlalchemy.relationship.config.db import Base
from andres.course.orm.sqlalchemy.relationship.models.student_course import student_course


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    title = Column(String(100), nullable=False)
    # Relación inversa: los estudiantes inscritos
    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )
    def __repr__(self):
        return f"Course(id={self.id}, code='{self.code}', title='{self.title}')"
