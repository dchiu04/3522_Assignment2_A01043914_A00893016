import abc
from candy import Candy

class CandyFactory(abc.Abc):
    @staticmethod
    def create():
        pass


class PumpkinToffee(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Halloween"
        lactose = False
        nuts = True
        #return Candy(theme, lactose, nuts)


class CandyCane(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Christmas"
        lactose = False
        nuts = False
        #return Candy(theme, lactose, nuts)


class CremeEggs(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Easter"
        number = 1
        #return Candy(theme, number)

