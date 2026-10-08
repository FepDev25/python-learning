from threading import Thread

from andres.bakery.bakery import Bakery


class Consumer(Thread):

    def __init__(self, bakery: Bakery):
        super().__init__()
        self.bakery = bakery

    def run(self):
        for _ in range(10):
            self.bakery.consume()