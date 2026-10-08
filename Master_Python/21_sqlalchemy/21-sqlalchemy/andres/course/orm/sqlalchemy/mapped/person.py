from sqlalchemy import Column, Integer, String

from andres.course.orm.sqlalchemy.config.db import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<Person(id={self.id}, name='{self.name}', lastname='{self.lastname}', email='{self.email}', age={self.age})>"
