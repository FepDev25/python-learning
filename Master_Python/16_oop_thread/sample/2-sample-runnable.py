from threading import Thread

from andres.sample.oop.thread.travel_task import TravelTask

thread1 = Thread(target=TravelTask('Isla de Pascua').run)
thread1.start()

Thread(target=TravelTask('Islas Maldivas').run).start()
Thread(target=TravelTask('Isla Juan Fernandez').run).start()
Thread(target=TravelTask('Isla de Chiloe').run).start()
Thread(target=TravelTask('Isla Robinson Crusoe').run).start()