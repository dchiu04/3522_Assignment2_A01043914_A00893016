import threading
import time
import city_processor


class CityOverheadTimeQueue:

    def __init__(self):
        self._data_queue = []
        self._access_queue_lock = threading.Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        # with self._access_queue_lock:
        self._access_queue_lock.acquire()
        try:
            self._data_queue.append(overhead_time)
        finally:
            self._access_queue_lock.release()

    def get(self) -> city_processor.CityOverheadTimes:
        #with self._access_queue_lock:
        self._access_queue_lock.acquire()
        temp = None

        try:
            temp = self._data_queue[0]
            del (self._data_queue[0])
        finally:
            self._access_queue_lock.release()
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
                print("ProducerThread:", city_processor.ISSDataRequest.get_overhead_pass(c))
                count += 1
            else:
                count = 0
                time.sleep(1)
                print("slept for 1 second")


class ConsumerThread(threading.Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self._data_incoming = True

    def run(self) -> None:
        while self._data_incoming or self._queue.len() > 0:
            if self._queue.len() == 0:
                self._data_incoming = False
            try:
                item = self._queue.get()
            except IndexError:
                item = None
            print("ConsumerThread:", item)
            if self._queue.len() == 0:
                time.sleep(0.75)
                print("slept for 0.75 seconds")
            else:
                time.sleep(0.5)
                print("slept for 0.5 seconds")


def main():
    filepath = "city_locations_test.xlsx"
    db = city_processor.CityDatabase(filepath)

    q = CityOverheadTimeQueue()

    x = int((len(db.city_db) / 3))
    y = x * 2
    prod = ProducerThread(db.city_db[0:x], q)
    prod2 = ProducerThread(db.city_db[x:y], q)
    prod3 = ProducerThread(db.city_db[y:], q)
    cons = ConsumerThread(q)

    threads = [prod, cons, prod2, prod3]

    # Add threads to thread list
    prod.start()
    cons.start()
    prod2.start()
    prod3.start()


    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")



if __name__ == "__main__":
    main()
