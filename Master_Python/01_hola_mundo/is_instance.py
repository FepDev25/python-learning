class Person:
    pass

class Animal:
    pass

class Dog(Animal):
    pass

num = 10
text = 'Creando un objeto de la clase str'
num_decimal = 3.1415

b1 = isinstance(text, str)
print(f'text es del tipo str = {b1}')

b2 = isinstance(num, int)
print(f'num es del tipo int = {b2}')

b3 = isinstance(num_decimal, float)
print(f'{num_decimal} el del tipo float = {b3}')

b4 = isinstance(num, str)
print(f'{num} el de tipo str? = {b4}')

b5 = isinstance(b4, bool)
print(f'{b4} es del tipo bool? = {b5}')

data = 3.14
b6 = isinstance(data, (int, float))
print(f'{data} es del tipo int o float = {b6}')

b7 = isinstance(text, (int, float))
print(f'{text} es del tipo int o float = {b7}')

dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Person))

andres = Person()
print(isinstance(andres, Person))
print(isinstance(andres, Dog))
print(isinstance(andres, Animal))
print(isinstance(andres, (Animal, Person)))
