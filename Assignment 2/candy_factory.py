import abc
from candy import Candy

class CandyFactory(abc.ABC):
    @staticmethod
    def create():
        pass


class PumpkinToffeeFactory(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Halloween"
        lactose = False
        nuts = True
        #return Candy(theme, lactose, nuts)


class CandyCaneFactory(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Christmas"
        lactose = False
        nuts = False
        #return Candy(theme, lactose, nuts)


class CremeEggsFactory(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Easter"
        number = 1
        #return Candy(theme, number)

