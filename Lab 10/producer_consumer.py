import threading

import city_processor
from consumer_thread import ConsumerThread
from producer_thread import ProducerThread


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


def main():
    filepath = "city_locations.xlsx"
    db = city_processor.CityDatabase(filepath)

    # for x in db.city_db:
    #     print(x)
    city = db.city_db[1]
    print(city)
    city_overhead1 = city_processor.ISSDataRequest.get_overhead_pass(city)
    q = CityOverheadTimeQueue()

    prod = ProducerThread(city, q)
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
