class Amazon:
    def __init__(self):
        self._inventory = []

    def process_orders(self):
        print("Processing orders")

    def check_inv(self):
        print("checking inv")


def menu(self):
    user = int(input("----Amazon Menu----\n1)Process Web Orders"
                     "\n2)Check Inventory\n3)Exit\n"))
    if user == 1:
        self.process_orders()
    elif user == 2:
        self.check_inv()
    else:
        print("Goodbye.")
        return


def main():
    store = Amazon()
    menu(store)


if __name__ == '__main__':
    main()
