from sqlalchemy import Integer, String, Column, ForeignKey

from andres.course.orm.sqlalchemy.relationship.config.db import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    def __repr__(self):
        return f"Address(id={self.id}, street='{self.street}', city='{self.city}')"
