from invoice.app.models.customer import Customer
from invoice.app.models.invoice import Invoice
from invoice.app.models.item import Item
from invoice.app.models.product import Product

customer = Customer('Andres', 'Guzman', '44444-5')

description = input('Ingrese una descripcion de la factura: ')
invoice = Invoice(description, customer)

for _ in range(5):
    name = input('Ingrese un nombre de producto: ')
    price = float(input('Ingrese el precio del producto: '))
    product = Product(name, price)

    quantity = int(input('Ingrese la cantidad: '))
    invoice.add_item(Item(quantity, product))

print(invoice)

