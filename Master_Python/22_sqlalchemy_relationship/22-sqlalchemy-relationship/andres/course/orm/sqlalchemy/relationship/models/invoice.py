from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from andres.course.orm.sqlalchemy.relationship.config.db import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    # relación unidireccional: desde Invoice se puede acceder a Customer
    customer = relationship("Customer", back_populates="invoices")

    def __repr__(self):
        return f"Invoice(id={self.id}, amount={self.amount}, customer={self.customer})"
