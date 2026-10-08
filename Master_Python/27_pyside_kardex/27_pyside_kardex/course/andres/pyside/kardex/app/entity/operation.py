from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date, Numeric

from course.andres.pyside.kardex.app.config.db import Base

class Operation(Base):
    __tablename__ = "financial_operation"
    __allow_unmapped__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    company: Mapped[str] = mapped_column(String(255), nullable=False)
    account_number: Mapped[str] = mapped_column(String(50), nullable=False)
    issuer: Mapped[str] = mapped_column(String(255), nullable=False)
    operation: Mapped[str] = mapped_column(String(50), nullable=False)
    movement_date: Mapped[Date] = mapped_column(Date, nullable=False)
    instrument: Mapped[str] = mapped_column(String(255), nullable=False)

    quantity: Mapped[float] = mapped_column(Numeric(18, 4), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(18, 6), nullable=False)

    balance: Optional[float] = None

    def __repr__(self) -> str:
        return (
            f"Operation(id={self.id}, company={self.company}, "
            f"account_number={self.account_number}, issuer={self.issuer}, "
            f"operation={self.operation}, movement_date={self.movement_date}, "
            f"instrument={self.instrument}, quantity={self.quantity}, price={self.price})"
        )