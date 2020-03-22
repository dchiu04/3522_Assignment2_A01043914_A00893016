import pandas as pd
from pathlib import Path

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
        all_orders = {}
        try:
            if Path(fn).is_file():
                orders = pd.read_excel(fn).to_dict(orient="record")
                for i in orders:
                    holiday = i.get("holiday")
                    item = i.get("item")
                    keys = ['description',
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
                    order = Order(i.get("order_number"), i.get("product_id"), item, i.get("name"),
                                  details)
                    OrderProcessor.factory_mapping(order, holiday, item)
                    all_orders[order.order_num] = [i.get('quantity'), order]
            else:
                raise FileNotFoundError("File was not found. Orders were not processed.")

        finally:
            return all_orders

    @staticmethod
    def factory_mapping(order, holiday, item):
        factory = factory_dict.get(item).get(holiday)
        order._factory = factory
