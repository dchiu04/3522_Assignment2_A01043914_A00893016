import pandas as pd
from pathlib import Path
from operator import itemgetter

from order import Order


# import order


class OrderProcessor:

    @staticmethod
    def read_file_to_orders(fn):
        all_orders = []
        try:
            if Path(fn).is_file():
                orders = pd.read_excel(fn).to_dict(orient="record")
                for i in orders:
                    order = Order(i.get("order_number"), i.get("product_id"), i.get("item"), i.get("name"),
                                  dict(list(i.items())[7:]), i.get("holiday"))
                    print(order)
                    all_orders.append(order)
            else:
                raise FileNotFoundError("File was not found.")

        finally:
            return all_orders

    @staticmethod
    def factory_mapping(order):

        pass

#
# def main():
#     OrderProcessor.read_file_to_orders("orders.xlsx")
#     OrderProcessor.factory_mapping(OrderProcessor)
#
#
# if __name__ == '__main__':
#     main()
