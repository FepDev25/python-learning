import time
from andres.sample.oop.thread.name_thread import NameThread

thread1 = NameThread('John Doe')
thread1.start()
# time.sleep(1 / 1000)

thread2 = NameThread('Andres Guzman')
thread2.start()

thread3 = NameThread('Maria Roe')
thread3.start()
print(f'Thread is alive {thread1.is_alive()}')
