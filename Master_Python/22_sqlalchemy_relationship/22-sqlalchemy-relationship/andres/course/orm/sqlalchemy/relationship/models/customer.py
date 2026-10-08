from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from andres.course.orm.sqlalchemy.relationship.config.db import Base
from andres.course.orm.sqlalchemy.relationship.models.address import Address
from andres.course.orm.sqlalchemy.relationship.models.invoice import Invoice

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # relación unidireccional: un cliente tiene muchas direcciones
    addresses = relationship("Address", cascade="all, delete-orphan")
    invoices = relationship("Invoice", cascade="all, delete-orphan", back_populates="customer")

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}')"
