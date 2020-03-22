from order_processor import OrderProcessor
import datetime


class Amazon:
    def __init__(self):
        self._orders = []
        self._inventory = {}

    def process_orders(self):
        user = input("Enter the name of the excel file to be processed(.xlsx): ")
        op = OrderProcessor()
        orders = op.read_file_to_orders(user + ".xlsx")

        for i in orders:
            self._orders.append(orders[i])
            kwargs = {'name': orders[i][1].name,
                      'desc': orders[i][1].details['description'],
                      'product_id': orders[i][1].product_id,
                      'has_batteries': orders[i][1].details['has_batteries'],
                      'min_age': orders[i][1].details['min_age'],
                      'dimensions': orders[i][1].details['dimensions'],
                      'num_rooms': orders[i][1].details['num_rooms'],
                      'speed': orders[i][1].details['speed'],
                      'jump_height': orders[i][1].details['jump_height'],
                      'has_glow': orders[i][1].details['has_glow'],
                      'spider_type': orders[i][1].details['spider_type'],
                      'num_sound': orders[i][1].details['num_sound'],
                      'colour': orders[i][1].details['colour'],
                      'has_lactose': orders[i][1].details['has_lactose'],
                      'has_nuts': orders[i][1].details['has_nuts'],
                      'variety': orders[i][1].details['variety'],
                      'pack_size': orders[i][1].details['pack_size'],
                      'stuffing': orders[i][1].details['stuffing'],
                      'size': orders[i][1].details['size'],
                      'fabric': orders[i][1].details['fabric']
                      }

            item = orders[i][1].factory.create(orders[i][1].factory, **kwargs)
            # Initializing inventory quantity
            self.restock_inv(item, i - 1, kwargs)
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
                print("Product ID", i, "is: In Stock(", len(k), ")")
            elif 10 > len(k) > 3:
                print("Product ID", i, "is: Low stock(", len(k), ")")
            elif 0 < len(k) <= 3:
                print("Product ID", i, "is: Very Low stock(", len(k), ")")
            else:
                print("Product ID", i, "is: Out of stock (0)")

    def print_report(self):
        date = datetime.datetime.now()
        with open("report.txt", "a") as file:
            file.write("\nAMAZON - DAILY TRANSACTION REPORT (DRT)\n"
                       + str(date) + "\n\n")
            print("AMAZON - DAILY TRANSACTION REPORT (DRT)\n"
                  + str(date) + "\n\n")
            for i, k in self._orders:
                temp = "Order: {}, Item: {}, Product ID: {}, Name {}, Quantity: {}"
                print(temp.format(k.order_num, k.item_type, k.product_id, k.name, i))
                file.write(temp.format(k.order_num, k.item_type, k.product_id, k.name, i))
                file.write("\n")

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
