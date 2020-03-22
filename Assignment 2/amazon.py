from order_processor import OrderProcessor
import datetime


class Amazon:
    def __init__(self):
        self._orders = []
        self._inventory = {}

    def process_orders(self):
        user = input("Enter the name of the excel file to be processed(.xlsx): ")
        op = OrderProcessor()
        self._orders = op.read_file_to_orders(user + ".xlsx")

        for i in self._orders:
            kwargs = {'name': self._orders[i][1].name,
                      'desc': self._orders[i][1].details['description'],
                      'product_id': self._orders[i][1].product_id,
                      'has_batteries': self._orders[i][1].details['has_batteries'],
                      'min_age': self._orders[i][1].details['min_age'],
                      'dimensions': self._orders[i][1].details['dimensions'],
                      'num_rooms': self._orders[i][1].details['num_rooms'],
                      'speed': self._orders[i][1].details['speed'],
                      'jump_height': self._orders[i][1].details['jump_height'],
                      'has_glow': self._orders[i][1].details['has_glow'],
                      'spider_type': self._orders[i][1].details['spider_type'],
                      'num_sound': self._orders[i][1].details['num_sound'],
                      'colour': self._orders[i][1].details['colour'],
                      'has_lactose': self._orders[i][1].details['has_lactose'],
                      'has_nuts': self._orders[i][1].details['has_nuts'],
                      'variety': self._orders[i][1].details['variety'],
                      'pack_size': self._orders[i][1].details['pack_size'],
                      'stuffing': self._orders[i][1].details['stuffing'],
                      'size': self._orders[i][1].details['size'],
                      'fabric': self._orders[i][1].details['fabric']
                      }
            item = self._orders[i][1].factory.create(self._orders[i][1].factory, **kwargs)

            # Initializing inventory quantity
            self.restock_inv(item, i, kwargs)
        print("Successfully processed orders.")

    def check_quantity(self, product_id, quantity_ordered):
        quantity = len(self._inventory[product_id])
        if quantity > quantity_ordered:
            return True
        return False

    def restock_inv(self, item, i, kwargs):
        try:
            # Inventory has enough items, no need to create new ones
            if self.check_quantity(item.product_id, self._orders[i][0]):
                for x in range(self._orders[i][0]):
                    item = self._orders[i][1].factory.create(self._orders[i][1].factory, **kwargs)
                    self._inventory[item.product_id].pop()
            else:
                # Create only the left over items after minusing the initial value (100) from the order quantity
                for x in range(100 - self._orders[i][0]):
                    item = self._orders[i][1].factory.create(self._orders[i][1].factory, **kwargs)
                    self._inventory[item.product_id].append(item)
        except KeyError:
            # Inventory did not have the item already (initial)
            self._inventory[item.product_id] = []
            for x in range(100 - self._orders[i][0]):
                item = self._orders[i][1].factory.create(self._orders[i][1].factory, **kwargs)
                self._inventory[item.product_id].append(item)

    def check_inv(self):
        for i, k in self._inventory.items():
            if len(k) >= 10:
                print("Product ID", i, "is: In Stock(",len(k),")")
            elif 10 > len(k) > 3:
                print("Product ID", i, "is: Low stock(",len(k),")")
            elif 0 < len(k) <= 3:
                print("Product ID", i, "is: Very Low stock(",len(k),")")
            else:
                print("Out of stock (0)")

    def error_handle(self):
        for x in self._inventory

    def print_report(self):
        date = datetime.datetime.now()
        print("AMAZON - DAILY TRANSACTION REPORT (DRT)\n"
              + str(date) + "\n\n")

    def menu(self):
        cont = True
        while cont:
            user = int(input("----Amazon Menu----\n1)Process Web Orders"
                             "\n2)Check Inventory\n3)Exit\n"))
            if user == 1:
                self.process_orders()
            elif user == 2:
                self.check_inv()
            else:
                self.print_report()
                cont = False
                return


def main():
    store = Amazon()
    store.menu()


if __name__ == '__main__':
    main()
