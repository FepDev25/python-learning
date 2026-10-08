import mysql.connector
from mysql.connector import Error
from threading import Lock

class DatabaseConnection:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        # Singleton con bloqueo para ser thread-safe
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host="localhost", user="root", password="sasa1234", database="python_course"):
        if not hasattr(self, "_connection"):
            try:
                self._connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
                print("Conexión establecida con la base de datos.")
            except Error as e:
                print("Error al conectar:", e)
                self._connection = None

    def get_connection(self):
        return self._connection

    def close_connection(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
            print("Conexión cerrada.")
            self._connection = None
            DatabaseConnection._instance = None