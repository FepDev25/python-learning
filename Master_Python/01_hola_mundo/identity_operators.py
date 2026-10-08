
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)
print(x is z)
print(z is y)
print(z is not y)

class Invoice:
    name: str
    def __eq__(self, __value):
        return self.name == __value.name

a = Invoice()
a.name = 'compras oficina'
b = Invoice()
b.name = 'compras oficina'
print(a is b)
print(a is not b)
c = b
print(c is b)

print(a == b)

i = 'hola'
j = 'hola'
print(i is j)
print(i == j)

k = 20
m = 20
print(k is m)
print(k == m)
