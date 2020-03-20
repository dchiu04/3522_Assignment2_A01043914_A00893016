from order_processor import OrderProcessor
import datetime


class Amazon:
    def __init__(self):
        self._inventory = []

    def process_orders(self):
        user = input("Enter the name of the excel file to be processed(.xlsx): ")
        op = OrderProcessor()
        self._inventory = op.read_file_to_orders(user + ".xlsx")

        for i in self._inventory:
            # print(i.details['has_batteries'])
            kwargs = {'quantity': i.details['quantity'],
                      'has_batteries': i.details['has_batteries'],
                      'min_age': i.details['min_age'],
                      'dimensions': i.details['dimensions'],
                      'num_rooms': i.details['num_rooms'],
                      'speed': i.details['speed'],
                      'jump_height': i.details['jump_height'],
                      'has_glow': i.details['has_glow'],
                      'spider_type': i.details['spider_type'],
                      'num_sound': i.details['num_sound'],
                      'colour': i.details['colour'],
                      'has_lactose': i.details['has_lactose'],
                      'has_nuts': i.details['has_nuts'],
                      'variety': i.details['variety'],
                      'pack_size': i.details['pack_size'],
                      'stuffing': i.details['stuffing'],
                      'size': i.details['size'],
                      'fabric': i.details['fabric']
                      }
            for key, value in kwargs.items():
                print(key, value)
            i.factory.create(kwargs)
        print("finished processing orders")

    def restock_inv(self, prod_id):
        for i in self._inventory:
            if i.prod_id == prod_id:
                print(i.name + " " + i.prod_id)
                # if i.quantity == 0:
                #     i.quantity += 100
                #     print("increased quantity by 100")

        # obj = list(filter(lambda inventory: inventory['product_id'] == prod_id, self._inventory))

        # print(self._inventory[0].product_id)

    def check_inv(self):
        pass
        # for i in self._inventory:
        #     if prod_id == i:
        #         if i.value == 0:
        #             self._inventory[i].value += 100

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
                self.restock_inv("C7777C")
            else:
                self.print_report()
                cont = False
                return


def main():
    store = Amazon()
    store.menu()


if __name__ == '__main__':
    main()
