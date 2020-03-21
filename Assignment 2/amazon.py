from order_processor import OrderProcessor
import datetime


class Amazon:
    def __init__(self):
        self._inventory = {}

    def process_orders(self):
        user = input("Enter the name of the excel file to be processed(.xlsx): ")
        op = OrderProcessor()
        orders = op.read_file_to_orders(user + ".xlsx")

        # print("SHOULD BE PRINTING ORDERS")
        # print(orders)
        for i in orders:
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

            # key is the product id, value is the quantity
            # print(item)

            item = orders[i][1].factory.create(orders[i][1].factory, **kwargs)
            # CREATE 100 OF EACH ORDER ITEM HERE. old method no work
            # Initializing inventory quantity
            print(item.product_id)
            try:
                if self.check_quantity(item.product_id, orders[i][0]):
                    for x in range(orders[i][0]):
                        item = orders[i][1].factory.create(orders[i][1].factory, **kwargs)
                        self._inventory[item.product_id].pop()
                else:
                    for x in range(100 - orders[i][0]):
                        item = orders[i][1].factory.create(orders[i][1].factory, **kwargs)
                        self._inventory[item.product_id].append(item)
            except KeyError:
                self._inventory[item.product_id] = []
                for x in range(100 - orders[i][0]):
                    item = orders[i][1].factory.create(orders[i][1].factory, **kwargs)
                    self._inventory[item.product_id].append(item)

        # for (key, value) in self._inventory:
        #     print(key, value)
        #     order.factory.create(kwargs)
        print("Successfully processed orders.")

    def check_quantity(self, product_id, quantity_ordered):
        quantity = len(self._inventory[product_id])
        if quantity > quantity_ordered:
            return True
        return False

    # def init_quantity(self, product_id, quantity_ordered):
    #     quantity = 0
    #     try:
    #         quantity = self._inventory[product_id][0]
    #     except TypeError:
    #         quantity = 0
    #     except KeyError:
    #         quantity = 0
    #     finally:
    #         if quantity > quantity_ordered:
    #             return True
    #         else:
    #             return False

    # def restock_inv(self, prod_id):
    #     for i in self._inventory:
    #         if i.prod_id == prod_id:
    #             print(i.name + " " + i.prod_id)
    #
    #             # THIS CODE HERE CAN BE FOR RESTOCK_INV()
    #             # if i.quantity == 0:
    #             #     i.quantity += 100
    #             #     print("increased quantity by 100")
    #             # [print(d) for d in self._inventory if d['item'] == 'Toy' and d['holiday'] == 'Christmas']
    #             # for i in self._inventory:
    #             #     if prod_id == i:
    #             #         if i.value == 0:
    #             #             self._inventory[i].value += 100

    def check_inv(self):
        for i, k in self._inventory.items():
            print(len(k))
            if len(k) >= 10:
                print("In Stock (10 or more)")
            elif 10 > len(k) > 3:
                print("Low stock (less than 10 and bigger than 3)")
            elif 0 < len(k) <= 3:
                print("Very Low stock (less than 3")
            else:
                print("Out of stock (0)")

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
    # for i, k in store._inventory.items():
    #     print(k)
    #     for x in k:
    #         print(x)

if __name__ == '__main__':
    main()
