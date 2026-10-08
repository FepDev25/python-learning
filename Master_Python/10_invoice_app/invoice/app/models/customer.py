class Customer:

    def __init__(self, name: str, lastname: str, tax_id: str):
        self.__name = name
        self.__lastname = lastname
        self.__tax_id = tax_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    def __str__(self):
        return f'Cliente: {self.name} {self.lastname}\t NIF: {self.tax_id}\n'

    @property
    def tax_id(self):
        return self.__tax_id

