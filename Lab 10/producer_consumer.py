import threading
import city_processor


class CityOverheadTimeQueue:
    """
        Queue data structure holding city overhead times (duration, risetimes).
        Includes methods to put and get data, as well as returning the length of the queue.
    """

    def __init__(self):
        self._data_queue = []
        self._access_queue_lock = threading.Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
            Appends data to the queue using locks.
        :param overhead_time: CityOverheadTimes dictionary with duration and risetimes
        """

        # Changes state of the lock to "locked"
        self._access_queue_lock.acquire()
        try:
            self._data_queue.append(overhead_time)
        finally:
            # Changes state of the lock back to "unlocked" once data alteration is finished
            self._access_queue_lock.release()

    def get(self) -> city_processor.CityOverheadTimes:
        """
            Returns the data at the first index (FIFO) and
            removes it from the queue.
        :return: data at the first index of the queue
        """

        # Changes state of the lock to "locked"
        self._access_queue_lock.acquire()
        temp = None

        try:
            temp = self._data_queue[0]
            del (self._data_queue[0])
        finally:
            # Change state of the lock back to "unlocked" once data alteration is finished
            self._access_queue_lock.release()
            return temp

    def len(self) -> int:
        """
            Returns the length of the queue
        :return: int corresponding to the length
        """
        return len(self._data_queue)


class ProducerThread(threading.Thread):
    """
        Thread that produces the data.
    """

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self._cities = cities
        self._queue = queue

    def run(self) -> None:
        """
            Starts the thread and produces the data.
        """
        count = 0

        for c in self._cities:
            if count < 5:
                self._queue.put(city_processor.ISSDataRequest.get_overhead_pass(c))
                print("ProducerThread:", c)
                count += 1
            else:
                count = 0
                time.sleep(1)
                print("ProducerThread: Slept for 1 second")


class ConsumerThread(threading.Thread):
    """
        Thread that consumes the data.
    """
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self._data_incoming = True

    def run(self) -> None:
        """
            Starts the thread that consumes the data.
        """

        while self._data_incoming or self._queue.len() > 0:
            try:
                item = self._queue.get()
                print("Consumer is consuming from the thread, Queue has", self._queue.len(), "elements left")
            except IndexError:
                item = None
            if item is None:
                time.sleep(0.5)
                print("ConsumerThread: Empty Queue")
                print("ConsumerThread: Slept for 0.5 seconds")
            else:
                print("ConsumerThread:", item)
                time.sleep(0.5)
                print("ConsumerThread: Slept for 0.5 seconds")
            if self._queue.len() == 0:
                time.sleep(0.75)
                print("ConsumerThread: Slept for 0.75 seconds")


def main():
    filepath = "city_locations_test.xlsx"
    db = city_processor.CityDatabase(filepath)
    q = CityOverheadTimeQueue()
    q.get()
    # Dividing up the database so each one gets approximately the same amount of data
    x = int((len(db.city_db) / 3))
    y = x * 2

    # Initializing threads
    prod = ProducerThread(db.city_db, q)
    prod2 = ProducerThread(db.city_db[x:y], q)
    prod3 = ProducerThread(db.city_db[y:], q)
    cons = ConsumerThread(q)
    threads = [prod, prod2, prod3]

    prod.start()
    cons.start()
    prod2.start()
    prod3.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    cons._data_incoming = False
    cons.join()
    print("All threads have completed their run time.")


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("Total duration %s seconds" % (time.time() - start_time))
