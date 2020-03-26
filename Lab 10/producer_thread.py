import time
from threading import Thread

import city_processor
from producer_consumer import CityOverheadTimeQueue


class ProducerThread(Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self._cities = cities
        self._queue = queue

    def run(self) -> None:
        count = 0

        for c in self._cities:
            if count < 5:
                city_processor.ISSDataRequest.get_overhead_pass(c)


                count += 1
            else:
                count = 0
                time.sleep(1)
