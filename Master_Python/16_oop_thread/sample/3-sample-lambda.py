import time
from random import random
from threading import Thread, current_thread

from andres.sample.oop.thread.travel_task import TravelTask

def travel_task():
    for i in range(10):
        print(f'{i} - {current_thread().name}')
        time.sleep(random())
    print(f'Finalmente moy a viajar a: {current_thread().name}')

travel = lambda: travel_task()

thread1 = Thread(target=travel, name='Isla de Pascua')
thread1.start()
thread2 = Thread(target=travel, name='Islas Maldivas')
thread2.start()
thread3 = Thread(target=travel, name='Isla Juan Fernandez')
thread3.start()
thread4 = Thread(target=travel, name='Isla de Chiloe')
thread4.start()
thread5 = Thread(target=travel, name='Isla Robinson Crusoe')
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

# time.sleep(7)
print('Continuando con la ejecucion del thread principal')