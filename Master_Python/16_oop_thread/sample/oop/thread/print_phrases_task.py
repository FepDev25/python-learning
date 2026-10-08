from dataclasses import dataclass
from multiprocessing import Lock

from andres.sample.oop.thread.funtions import print_phrases

@dataclass
class PrintPhrasesTask:
    phrase1: str
    phrase2: str

    def __call__(self) -> None:
        print_phrases(self.phrase1, self.phrase2)

