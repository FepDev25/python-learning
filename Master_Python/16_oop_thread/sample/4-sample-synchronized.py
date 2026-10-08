from threading import Thread

from andres.sample.oop.thread.print_phrases_task import PrintPhrasesTask

t1 = Thread(target=PrintPhrasesTask('Hola', 'que tal!'))
t1.start()

t2 = Thread(target=PrintPhrasesTask('Quien eres', 'tu?'))
t2.start()

t3 = Thread(target=PrintPhrasesTask('Muchas', 'gracias amigo!'))
t3.start()

