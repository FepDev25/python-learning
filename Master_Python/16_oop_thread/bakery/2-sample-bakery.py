from dataclasses import dataclass
from queue import Queue
from threading import Condition, Thread
import random
import time

@dataclass
class Bakery:
    bread: str = ''

    def __post_init__(self):
        self.queue = Queue(maxsize=1)

    def bake(self, dough: str):
        self.queue.put(dough)
        print(f'Panadero hornea: {self.bread}')

    def consume(self):
        self.bread = self.queue.get()
        print(f'Cliente consume: {self.bread}')

class Baker(Thread):

    def __init__(self, bakery: Bakery):
        super().__init__()
        self.bakery = bakery

    def run(self):
        for i in range(10):
            self.bakery.bake(f'Pan num: {i}')
            time.sleep(random.uniform(0.5, 2.0))

class Consumer(Thread):

    def __init__(self, bakery: Bakery):
        super().__init__()
        self.bakery = bakery

    def run(self):
        for _ in range(10):
            self.bakery.consume()

bakery = Bakery()

baker = Baker(bakery)
consumer = Consumer(bakery)
consumer.start()
baker.start()