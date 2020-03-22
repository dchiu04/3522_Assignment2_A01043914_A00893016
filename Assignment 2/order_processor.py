import math

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
                (message, condition) = OrderProcessor.error_handle(order, holiday)
                if condition:
                    print(order.order_num)
                    print("pass")
                    all_orders[order.order_num] = [i.get('quantity'), order]
                else:
                    print(message)
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

    # @staticmethod
    # def error_handle(order, holiday):
    #     if ErrorHandler.error_check(holiday, order, order.details):
    #         return True
    #             # file.write(temp.format(i.order_num, i.item_type, i.product_id, i.name, i))
    #             # file.write("\n")
    #     else:
    #         return False

    @staticmethod
    def error_handle(order, holiday):
        print(order.details['colour'])
        try:
            if holiday == 'Christmas' or holiday == 'Easter' or \
                    holiday == 'Halloween':
                pass
            else:
                return "holiday can only be ""Christmas"" or ""Easter"" or ""Halloween", False
        except TypeError:
            return "holiday can only be ""Christmas"" or ""Easter"" or ""Halloween", False
        try:
            if order.item_type == 'Toy' or order.item_type == 'StuffedAnimal' or \
                    order.item_type == 'Candy':
                pass
            else:
                return "item can only be ""Toy"" or ""StuffedAnimal"" or ""Candy", False
        except TypeError:
            return "item can only be ""Toy"" or ""StuffedAnimal"" or ""Candy", False
        try:
            if order.details['has_batteries'] == 'Y' or order.details['has_batteries'] == 'N' \
                    or math.isnan(order.details['has_batteries']):
                pass
            else:
                return "has_batteries can only be ""Y"" or ""N", False
        except TypeError:
            return "has_batteries can only be ""Y"" or ""N", False
        try:
            if order.details['min_age'] > 0 or math.isnan(order.details['min_age']):
                pass
            else:
                return "min_age can only be int greater than 0", False
        except TypeError:
            return "min_age can only be int greater than 0", False
        try:
            if order.details['num_rooms'] > 0 or math.isnan(order.details['num_rooms']):
                pass
            else:
                return "num_rooms can only be int greater than 0", False
        except TypeError:
            return "num_rooms can only be int greater than 0", False
        try:
            if order.details['speed'] > 0 or math.isnan(order.details['speed']):
                pass
            else:
                return "speed can only be int greater than 0", False
        except TypeError:
            return "speed can only be int greater than 0", False
        try:
            if order.details['jump_height'] > 0 or math.isnan(order.details['jump_height']):
                pass
            else:
                return "jump_height can only be int greater than 0", False
        except TypeError:
            return "jump_height can only be int greater than 0", False
        try:
            if order.details['has_glow'] == 'Y' or order.details['has_glow'] == 'N' \
                    or math.isnan(order.details['has_glow']):
                pass
            else:
                return "has_glow can only be ""Y"" or ""N", False
        except TypeError:
            return "has_glow can only be ""Y"" or ""N", False
        try:
            if order.details['spider_type'] == 'Tarantula' or order.details['spider_type'] == 'Wolf Spider' \
                    or math.isnan(order.details['spider_type']):
                pass
            else:
                return "spider_type can only be ""Tarantula"" or ""Wolf Spider", False
        except TypeError:
            return "spider_type can only be ""Tarantula"" or ""Wolf Spider", False
        try:
            if order.details['num_sound'] > 0 or math.isnan(order.details['num_sound']):
                pass
            else:
                return "num_sound can only be int greater than 0", False
        except TypeError:
            return "num_sound can only be int greater than 0", False
        try:
            if order.details['colour'] == 'Grey' or order.details['colour'] == 'Orange' or order.details[
                'colour'] == 'Green' or order.details['colour'] == 'Pink' or order.details['colour'] == 'Red' \
                    or math.isnan(order.details['colour']):
                pass
            else:
                return "colour can only be ""Grey"" or ""Orange"" or ""Green"" or ""Pink"" or ""Red", False
        except TypeError:
            return "colour can only be ""Grey"" or ""Orange"" or ""Green"" or ""Pink"" or ""Red", False
        try:
            if order.details['has_lactose'] == 'Y' or order.details['has_lactose'] == 'N' \
                    or math.isnan(order.details['has_lactose']):
                pass
            else:
                return "has_lactose can only be ""Y"" or ""N", False
        except TypeError:
            return "has_lactose can only be ""Y"" or ""N", False
        try:
            if order.details['has_nuts'] == 'Y' or order.details['has_nuts'] == 'N' \
                    or math.isnan(order.details['has_nuts']):
                pass
            else:
                return "has_nuts can only be ""Y"" or ""N", False
        except TypeError:
            return "has_nuts can only be ""Y"" or ""N", False
        try:
            if order.details['variety'] == 'Sea Salt' or math.isnan(order.details['variety']):
                pass
            else:
                return "variety can only be ""Sea Salt", False
        except TypeError:
            return "variety can only be ""Sea Salt", False
        try:
            if order.details['pack_size'] > 0 or math.isnan(order.details['pack_size']):
                pass
            else:
                return "pack_size can only be int greater than 0", False
        except TypeError:
            return "pack_size can only be int greater than 0", False
        try:
            if order.details['stuffing'] == 'Polyester Fibrefill' or order.details['stuffing'] == 'Wool' \
                    or math.isnan(order.details['stuffing']):
                pass
            else:
                return "stuffing can only be ""Polyester Fibrefill"" or ""Wool", False
        except TypeError:
            return "stuffing can only be ""Polyester Fibrefill"" or ""Wool", False
        try:
            if order.details['size'] == 'S' or order.details['size'] == 'M' or order.details['size'] == 'L' \
                    or math.isnan(order.details['size']):
                pass
            else:
                return "size can only be ""S"" or ""M"" or ""L", False
        except TypeError:
            return "size can only be ""S"" or ""M"" or ""L", False
        try:
            if order.details['fabric'] == 'Linen' or order.details['fabric'] == 'Acrylic' or \
                    order.details['fabric'] == 'Cotton' or math.isnan(order.details['fabric']):
                pass
            else:
                return "fabric can only be ""Linen"" or ""Acrylic"" or ""Cotton", False
        except TypeError:
            return "fabric can only be ""Linen"" or ""Acrylic"" or ""Cotton", False
        return "", True
