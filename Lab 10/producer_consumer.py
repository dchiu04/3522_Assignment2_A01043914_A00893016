import city_processor


class ProducerConsumer:
    pass


class CityOverheadTimeQueue:

    def __init__(self):
        self._data_queue = []

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        self._data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        temp = self._data_queue[0]
        del (self._data_queue[0])
        return temp

    def len(self) -> int:
        return len(self._data_queue)


def main():
    filepath = "city_locations.xlsx"
    db = city_processor.CityDatabase(filepath)
    for x in db.city_db:
        print(x)
    city = db.city_db[0]
    print(city)

    # Failing on this line because json call fails? says no lat but there is a lat lol
    city_overhead1 = city_processor.ISSDataRequest.get_overhead_pass(city)
    q = CityOverheadTimeQueue()
    q.put(city_overhead1)
    print(q.len)
    print(q.get())


if __name__ == "__main__":
    main()
