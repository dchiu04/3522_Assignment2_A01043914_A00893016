import time
from threading import Thread

from producer_consumer import CityOverheadTimeQueue


class ConsumerThread(Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self._data_incoming = True

    def run(self) -> None:
        while self._data_incoming or self._queue.len() > 0:
            item = self._queue.get()
            print(item)
            if self._queue.len() == 0:
                time.sleep(0.75)
            else:
                time.sleep(0.5)
