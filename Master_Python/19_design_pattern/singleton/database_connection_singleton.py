class DatabaseConnectionSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando nueva conexión simulada a la base de datos...")
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        if not self.connected:
            print("Conectando a la base de datos (simulada)...")
            self.connected = True
        else:
            print("Ya existe una conexión activa.")

    def disconnect(self):
        if self.connected:
            print("Desconectando de la base de datos (simulada)...")
            self.connected = False
        else:
            print("No hay conexión activa.")
