import time
from threading import Thread

class NameThread(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f'se inicia el metodo run del hilo {self.name}')

        for i in range(10):
            time.sleep(10/1000)
            print(self.name)

        print(f'finaliza el hilo: {self.name}')