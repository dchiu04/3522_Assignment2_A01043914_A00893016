import pandas as pd


class OrderProcessor:

    @staticmethod
    def readFileToOrders(fileName):
        allOrders = pd.read_excel(fileName).to_dict(orient="record")
        for i in allOrders:
            print(i)

def main():
    OrderProcessor.readFileToOrders("orders.xlsx")


if __name__ == '__main__':
    main()
