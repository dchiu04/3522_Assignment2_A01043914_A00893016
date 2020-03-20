import pandas as pd
from pathlib import Path
from operator import itemgetter

from animal_factory import ReindeerFactory, BunnyFactory, SkeletonFactory
from candy_factory import CandyCaneFactory, CremeEggsFactory, PumpkinToffeeFactory
from order import Order
from toy_factory import SantaWorkshopFactory, SpiderFactory, RobotBunnyFactory

factory_dict = {"Toy": {"Christmas": SantaWorkshopFactory, "Easter": RobotBunnyFactory, "Halloween": SpiderFactory},
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
                    keys = ['quantity',
                            'has_batteries',
                            'min_age',
                            'dimensions',
                            'num_rooms',
                            'speed',
                            'jump_height',
                            'has_glow',
                            'spider_type',
                            'num_sound',
                            'colour',
                            'has_lactose',
                            'has_nuts',
                            'variety',
                            'pack_size',
                            'stuffing',
                            'size',
                            'fabric']
                    details = {x: i[x] for x in keys}
                    order = Order(i.get("order_number"), item, i.get("name"), i.get("product_id"),
                                  details)
                    OrderProcessor.factory_mapping(order, holiday, item)
                    # print(order.factory)
                    all_orders.append(order)
            else:
                raise FileNotFoundError("File was not found.")

        finally:
            return all_orders

    @staticmethod
    def factory_mapping(order, holiday, item):
        factory = factory_dict.get(item).get(holiday)
        print(factory)
        order._factory = factory
