import pandas as pd
from pathlib import Path

from animal_factory import ReindeerFactory, BunnyFactory, SkeletonFactory
from candy_factory import CandyCaneFactory, CremeEggsFactory, PumpkinToffeeFactory
from error_handler import ErrorHandler
from order import Order
from toy_factory import SantaWorkshopFactory, SpiderFactory, RobotBunnyFactory

factory_dict = {"Toy": {"Christmas": SantaWorkshopFactory, "Easter": RobotBunnyFactory, "Halloween": SpiderFactory},
                "StuffedAnimal": {"Christmas": ReindeerFactory, "Easter": BunnyFactory, "Halloween": SkeletonFactory},
                "Candy": {"Christmas": CandyCaneFactory, "Easter": CremeEggsFactory, "Halloween": PumpkinToffeeFactory}}


class OrderProcessor:
    def __init__(self):
        self._total_orders = {}

    def read_file_to_orders(self, fn):
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

                    # # Only add valid orders to the store
                    # if ErrorHandler.error_check(fn, self._all_orders[i]):
                    #     all_orders[order.order_num] = [i.get('quantity'), order]
                    all_orders[order.order_num] = [i.get('quantity'), order]
                    # Used to print out report only
                    self._total_orders[order.order_num] = [i.get('quantity'), order]
        finally:
            return all_orders

    @staticmethod
    def factory_mapping(self, order, holiday, item):
        factory = factory_dict.get(item).get(holiday)
        order._factory = factory

    # USED IN AMAZON TO PRINT BOTH VALID AND INVALID ORDERS
    def error_handle(self, file, i):
        if ErrorHandler.error_check(file, self._total_orders[i]):
            temp = "Order: {}, Item: {}, Product ID: {}, Name {}, Quantity: {}"
            # print(temp.format(k.order_num, k.item_type, k.product_id, k.name, i))
            file.write(temp.format(i.order_num, i.item_type, i.product_id, i.name, i))
            file.write("\n")
