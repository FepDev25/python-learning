import time
from threading import Lock

_lock = Lock()
def print_phrases(text: str, text2: str):
    with _lock:
        print(text, end=' ', flush=True)
        time.sleep(0.5)
        print(text2, flush=True)