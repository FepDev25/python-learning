from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from andres.course.orm.sqlalchemy.relationship.config.db import SessionLocal, Base, engine
from andres.course.orm.sqlalchemy.relationship.models.customer import Customer
from andres.course.orm.sqlalchemy.relationship.models.invoice import Invoice


Base.metadata.create_all(engine)

with SessionLocal() as session:
    try:
        # Hacemos un join directo entre Customer e Invoice
        stmt = (
            select(Customer, Invoice)
            .join(Invoice, Customer.id == Invoice.customer_id)
            .where(Customer.name == "Andrés Guzmán")
        )

        results = session.execute(stmt).all()

        print("\nFacturas del cliente:")
        for customer, invoice in results:
            print(f"{customer.name} → Factura #{invoice.id} - Monto: {invoice.amount}")

        # stmt = (
        #     select(Customer)
        #     .options(joinedload(Customer.invoices))  # aquí está el eager loading
        #     .where(Customer.name == "Andrés Guzmán")
        # )
        # customer = session.scalars(stmt).first()
        #
        # print(f"\nCliente: {customer.name}")
        # print("Facturas:")
        # for inv in customer.invoices:
        #     print(f" - Factura #{inv.id} - Monto: {inv.amount}")
    except SQLAlchemyError as e:
        session.rollback()
        print(e)