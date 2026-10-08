import random
import time
from threading import Thread

from andres.bakery.bakery import Bakery


class Baker(Thread):

    def __init__(self, bakery: Bakery):
        super().__init__()
        self.bakery = bakery

    def run(self):
        for i in range(10):
            self.bakery.bake(f'Pan num: {i}')
            time.sleep(random.uniform(0.5, 2.0))