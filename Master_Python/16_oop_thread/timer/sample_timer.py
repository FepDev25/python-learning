from datetime import datetime
from threading import current_thread, Timer
import time

counter = 3
interval = 6.0

def task():
    global counter

    if counter > 0:
        print(f'Tarea realizada en: {datetime.now()} nombre del thread: {current_thread()}')
        counter -= 1
        Timer(interval, task).start()
    else:
        print('Finaliza el tiempo')

timer = Timer(2.0, task)
timer.start()

print('Agendamos una tarea para 2 segundos mas ...')

timer.join()