from andres.bakery.bakery import Bakery
from andres.bakery.thread.baker import Baker
from andres.bakery.thread.consumer import Consumer

bakery = Bakery()

baker = Baker(bakery)
consumer = Consumer(bakery)
consumer.start()
baker.start()