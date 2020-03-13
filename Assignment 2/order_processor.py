import pandas as pd
from pathlib import Path
from operator import itemgetter

from animal_factory import ReindeerFactory, BunnyFactory, SkeletonFactory
from candy_factory import CandyCaneFactory, CremeEggsFactory, PumpkinToffeeFactory
from toy_factory import SantaFactory, RobotBunnyFactory, RCSpiderFactory
from order import Order


factory_dict = {"Toy": {"Christmas": SantaFactory, "Easter": RobotBunnyFactory, "Halloween": RCSpiderFactory},
                "StuffedAnimal": {"Christmas": ReindeerFactory, "Easter": BunnyFactory, "Halloween": SkeletonFactory},
                "Candy": {"Christmas": CandyCaneFactory, "Easter": CremeEggsFactory, "Halloween": PumpkinToffeeFactory}}


class OrderProcessor:

    @staticmethod
    def read_file_to_orders(fn):
        all_orders = []
        try:
            if Path(fn).is_file():
                orders = pd.read_excel(fn).to_dict(orient="record")
                for i in orders:
                    holiday = i.get("holiday")
                    item = i.get("item")
                    order = Order(i.get("order_number"), i.get("product_id"), item, i.get("name"),
                                  dict(list(i.items())[7:]))
                    OrderProcessor.factory_mapping(order, holiday, item)
                    print(order.factory)
                    all_orders.append(order)
            else:
                raise FileNotFoundError("File was not found.")

        finally:
            return all_orders

    @staticmethod
    def factory_mapping(order, holiday, item):
        factory = factory_dict.get(item).get(holiday)
        # print(factory)
        order._factory = factory

def main():
    orders = OrderProcessor.read_file_to_orders("orders.xlsx")
    # for i in orders:
    #     i.factory.create()
    # OrderProcessor.factory_mapping(OrderProcessor)


if __name__ == '__main__':
    main()
