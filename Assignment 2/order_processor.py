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

    @staticmethod
    def read_file_to_orders(fn):
        """
            Reads the given excel file and converts it into a dictionary.
        :param fn: given excel file
        :return: all_orders list of dictionary
        """

        all_orders = {}
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
                if OrderProcessor.error_handle(order, holiday):
                    print(order.order_num)
                    all_orders[order.order_num] = [i.get('quantity'), order]
                else:
                    print("fail")
                # all_orders[order.order_num] = [i.get('quantity'), order]
                # Used to print out report only

        return all_orders

    @staticmethod
    def factory_mapping(order, holiday, item):
        """
            Maps the correct holiday to the order item.
        :param self: OrderProcessor
        :param order: current Order being processed
        :param holiday: the string designating the event
        :param item: to be mapped
        """
        factory = factory_dict.get(item).get(holiday)
        order._factory = factory

    # USED IN AMAZON TO PRINT BOTH VALID AND INVALID ORDERS

    @staticmethod
    def error_handle(order, holiday):
        if ErrorHandler.error_check(holiday, order, order.details):
            return True
                # file.write(temp.format(i.order_num, i.item_type, i.product_id, i.name, i))
                # file.write("\n")
        else:
            return False
