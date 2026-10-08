from __future__ import annotations

from typing import List, Optional

from sqlalchemy import select, case, func
from sqlalchemy.orm import Session, sessionmaker

from course.andres.pyside.kardex.app.entity.operation import Operation
from course.andres.pyside.kardex.app.models.dto.operation_with_balance import OperationWithBalance
from course.andres.pyside.kardex.app.repositories.operation_repository import OperationRepository  # ajusta el import según tu ruta


class OperationRepositoryImpl(OperationRepository):

    def find_all_with_balance(self, offset: int = 0, limit: int = 100) -> List[OperationWithBalance]:
        with self._session_factory() as session:
            movs = (
                select(
                    Operation.id,
                    Operation.company,
                    Operation.account_number,
                    Operation.issuer,
                    Operation.operation,
                    Operation.movement_date,
                    Operation.instrument,
                    Operation.quantity,
                    case(
                        (Operation.operation.in_(("COSTO", 'COMPRA')), Operation.quantity),
                        (Operation.operation == 'VENTA', -Operation.quantity)
                    ).label('delta'),
                    Operation.price
                ).cte('movs')
            )

            stmt = (
                select(
                    movs.c.id,
                    movs.c.company,
                    movs.c.account_number,
                    movs.c.issuer,
                    movs.c.operation,
                    movs.c.movement_date,
                    movs.c.instrument,
                    movs.c.quantity,
                    func.sum(movs.c.delta).over(
                        partition_by=(
                            movs.c.company,
                            movs.c.account_number,
                            movs.c.instrument,
                        ),
                        order_by=(movs.c.movement_date,
                                  movs.c.id)
                    ).label('balance'),
                    movs.c.price,
                )
                .order_by(movs.c.movement_date, movs.c.id)
                .offset(offset)
                .limit(limit)
            )

            result = session.execute(stmt).all()

            return [
                OperationWithBalance(id=r.id,
                                     company=r.company,
                                     account_number=r.account_number,
                                     issuer=r.issuer,
                                     operation=r.operation,
                                     movement_date=r.movement_date,
                                     instrument=r.instrument,
                                     quantity=r.quantity,
                                     balance=r.balance,
                                     price=r.price
                                     )
                for r in result
            ]

    def __init__(self, session_factory: sessionmaker[Session]):
        self._session_factory = session_factory

    def find_by_id(self, operation_id: int) -> Optional[Operation]:
        with self._session_factory() as session:
            stmt = select(Operation).where(Operation.id == operation_id)
            result = session.execute(stmt)
            return result.scalar_one_or_none()

    def find_all(self, offset: int = 0, limit: int = 100) -> List[Operation]:
        with self._session_factory() as session:
            movs = (
                select(
                    Operation.id,
                    Operation.company,
                    Operation.account_number,
                    Operation.issuer,
                    Operation.operation,
                    Operation.movement_date,
                    Operation.instrument,
                    Operation.quantity,
                    case(
                        (Operation.operation.in_(("COSTO", 'COMPRA')), Operation.quantity),
                        (Operation.operation == 'VENTA', -Operation.quantity)
                    ).label('delta'),
                    Operation.price
                ).cte('movs')
            )

            balance_expr = func.sum(movs.c.delta).over(
                partition_by=(
                    movs.c.company,
                    movs.c.account_number,
                    movs.c.instrument,
                ),
                order_by=(movs.c.movement_date,
                          movs.c.id)
            )
            stmt = (
                select(Operation, balance_expr.label('balance'))
                .join_from(Operation, movs, Operation.id == movs.c.id)
                .order_by(movs.c.movement_date, movs.c.id)
                .offset(offset)
                .limit(limit)
            )

            result = session.execute(stmt).all()
            operations = []

            for op, balance in result:
                op.balance = balance
                operations.append(op)

            return operations
            # stmt = (
            #     select(Operation)
            #     .order_by(Operation.id)
            #     .offset(offset)
            #     .limit(limit)
            # )
            # result = session.execute(stmt)
            # return list(result.scalars().all())

    def save(self, operation: Operation) -> Operation:
        """
        If operation.id is None (or 0) -> INSERT.
        If operation.id has a value -> UPDATE via merge().
        Returns the managed instance.
        """
        with self._session_factory() as session:
            # INSERT
            if not getattr(operation, "id", None):
                session.add(operation)
                session.commit()
                session.refresh(operation)
                return operation

            # UPDATE (detached instance -> merge)
            managed_operation = session.merge(operation)
            session.commit()
            session.refresh(managed_operation)
            return managed_operation

    def delete(self, operation_id: int) -> bool:
        with self._session_factory() as session:
            db_operation = session.get(Operation, operation_id)
            if db_operation is None:
                return False

            session.delete(db_operation)
            session.commit()
            return True