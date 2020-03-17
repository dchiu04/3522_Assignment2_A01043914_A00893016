from order_processor import OrderProcessor
import datetime


class Amazon:
    def __init__(self):
        self._inventory = []

    def process_orders(self):
        user = input("Enter the name of the excel file to be processed(.xlsx): ")
        # op = OrderProcessor()
        # self._inventory = op.read_file_to_orders(user + ".xlsx")
        orders = OrderProcessor.read_file_to_orders("orders.xlsx")

        for i in orders:
            # print(i.details['has_batteries'])
            kwargs = {'has_batteries': i.details['has_batteries'],
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
                print(key,value)
            print("sdfsdfdsisfdiuhjewiufhwihewhiufwfwef2323232")
            i.factory.create(kwargs)
        #     i.factory.create(
        #         min_age=i.details['min_age'],
        #         dimensions=i.details['dimensions'],
        #         num_rooms=i.details['num_rooms'],
        #         speed=i.details['speed'],
        #         jump_height=i.details['jump_height'],
        #         has_glow=i.details['has_glow'],
        #         spider_type=i.details['spider_type'],
        #         num_sound=i.details['num_sound'],
        #         colour=i.details['colour'],
        #         has_lactose=i.details['has_lactose'],
        #         has_nuts=i.details['has_nuts'],
        #         variety=i.details['variety'],
        #         pack_size=i.details['pack_size'],
        #         stuffing=i.details['stuffing'],
        #         size=i.details['size'],
        #         fabric=i.details['fabric'],
        #         has_batteries=i.details['has_batteries']
        #     )
        # # OrderProcessor.factory_mapping(OrderProcessor)

    def check_inv(self):
        print("checking inv")

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
