from order_processor import OrderProcessor
import datetime


class Amazon:
    def __init__(self):
        self._inventory = []

    def process_orders(self):
        user = input("Enter the name of the excel file to be processed(.xlsx): ")
        op = OrderProcessor()
        orders = op.read_file_to_orders(user + ".xlsx")

        print("SHOULD BE PRINTING ORDERS")
        print(orders)
        for i in orders:
            kwargs = {'name': orders[i].details['name'],
                      'desc': orders[i].details['description'],
                      'prod_id': orders[i]._prod_id,
                      'has_batteries': orders[i].details['has_batteries'],
                      'min_age': orders[i].details['min_age'],
                      'dimensions': orders[i].details['dimensions'],
                      'num_rooms': orders[i].details['num_rooms'],
                      'speed': orders[i].details['speed'],
                      'jump_height': orders[i].details['jump_height'],
                      'has_glow': orders[i].details['has_glow'],
                      'spider_type': orders[i].details['spider_type'],
                      'num_sound': orders[i].details['num_sound'],
                      'colour': orders[i].details['colour'],
                      'has_lactose': orders[i].details['has_lactose'],
                      'has_nuts': orders[i].details['has_nuts'],
                      'variety': orders[i].details['variety'],
                      'pack_size': orders[i].details['pack_size'],
                      'stuffing': orders[i].details['stuffing'],
                      'size': orders[i].details['size'],
                      'fabric': orders[i].details['fabric']
                      }

            # key is the product id, value is the quantity
            item = orders[i][1].factory.create(orders[i][1].factory, **kwargs)
            print(item)

            # CREATE 100 OF EACH ORDER ITEM HERE. old method no work
            # # Initializing inventory quantity
            # if self.init_quantity(item, orders[i][0]):
            #     temp = self._inventory[item]
            #     self._inventory[item] = temp - orders[i][0]
            # else:
            #     self._inventory[item] = 100 - orders[i][0]

        for (key, value) in self._inventory:
            print(key, value)
        #     order.factory.create(kwargs)
        print("Successfully processed orders.")

    def restock_inv(self, prod_id):
        for i in self._inventory:
            if i.prod_id == prod_id:
                print(i.name + " " + i.prod_id)

                # THIS CODE HERE CAN BE FOR RESTOCK_INV()
                # if i.quantity == 0:
                #     i.quantity += 100
                #     print("increased quantity by 100")
                # [print(d) for d in self._inventory if d['item'] == 'Toy' and d['holiday'] == 'Christmas']
                # for i in self._inventory:
                #     if prod_id == i:
                #         if i.value == 0:
                #             self._inventory[i].value += 100

    def init_quantity(self, product_id, quantity_ordered):
        quantity = 0
        try:
            quantity = self._inventory[product_id][0]
        except TypeError:
            quantity = 0
        except KeyError:
            quantity = 0
        finally:
            if quantity > quantity_ordered:
                return True
            else:
                return False

    def check_inv(self):
        for i in self._inventory:
            if i._prod_details['quantity'] >= 10:
                print(i)
                print("In Stock (10 or more)")
            elif 10 > i._prod_details['quantity'] > 3:
                print(i)
                print("Low stock (less than 10 and bigger than 3)")
            elif i._prod_details['quantity'] < 3:
                print(i)
                print("Very Low stock (less than 3")
            else:
                print(i)
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
                # self.restock_inv("C7777C")
                self.check_inv()
            else:
                self.print_report()
                cont = False
                return


def main():
    store = Amazon()
    store.menu()
    for i in store._inventory:
        print(i._name)


if __name__ == '__main__':
    main()
