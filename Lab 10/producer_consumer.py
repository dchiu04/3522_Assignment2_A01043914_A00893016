import threading
import time

import city_processor

class CityOverheadTimeQueue:

    def __init__(self):
        self._data_queue = []
        self._access_queue_lock = threading.Lock()  # Not sure about this line, he wrote it in an example tho

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        with self._access_queue_lock:
            self._data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        with self._access_queue_lock:
            temp = self._data_queue[0]
            del (self._data_queue[0])
            return temp

    def len(self) -> int:
        return len(self._data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self._cities = cities
        self._queue = queue

    def run(self) -> None:
        count = 0

        for c in self._cities:
            if count < 5:
                self._queue.put(city_processor.ISSDataRequest.get_overhead_pass(c))
                count += 1
            else:
                count = 0
                time.sleep(1)


class ConsumerThread(threading.Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self._data_incoming = True

    def run(self) -> None:
        while self._data_incoming or self._queue.len() > 0:
            try:
                item = self._queue.get()
            except IndexError:
                item = None
            print(item)
            if self._queue.len() == 0:
                time.sleep(0.75)
            else:
                time.sleep(0.5)


def main():
    filepath = "city_locations_test.xlsx"
    db = city_processor.CityDatabase(filepath)

    # for x in db.city_db:
    #     print(x)
    city = db.city_db[1]
    print(city)
    city_overhead1 = city_processor.ISSDataRequest.get_overhead_pass(city)

    q = CityOverheadTimeQueue()
    print(city_overhead1)
    q.put(city_overhead1)

    prod = ProducerThread(db.city_db, q)
    cons = ConsumerThread(q)

    threads = []
    prod.start()
    cons.start()

    # Add threads to thread list
    threads.append(prod)
    threads.append(cons)

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")

    q.put(city_overhead1)
    print(q.len())
    print(q.get())


if __name__ == "__main__":
    main()
