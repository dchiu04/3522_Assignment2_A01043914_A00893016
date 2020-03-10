import pandas as pd
from pathlib import Path
from operator import itemgetter

#from order import Order

class OrderProcessor:

    def __init__(self):
        self._order_list = []

    def read_file_to_orders(self, fn):
        try:
            if Path(fn).is_file():
                all_orders = pd.read_excel(fn).to_dict(orient="record")
                for i in all_orders:
                    print(i)
            else:
                all_orders = []
                raise FileNotFoundError("File was not found.")

        finally:
            self._order_list = all_orders
        return all_orders

    def factory_mapping(self):
        #christmas_orders = list(map(itemgetter('Christmas'), self._order_list))
        # christmas_orders = [d['Christmas'] for d in self._order_list]
        # easter_orders = [d['Easter'] for d in self._order_list]
        # halloween_orders = [d['Halloween'] for d in self._order_list]
        # print(halloween_orders)
        # return christmas_orders
        pass
#
#
# def main():
#     OrderProcessor.read_file_to_orders(OrderProcessor,"orders.xlsx")
#     OrderProcessor.factory_mapping(OrderProcessor)
#
#
# if __name__ == '__main__':
#     main()
