import abc
from candy import Candy

class CandyFactory(abc.Abc):
    @staticmethod
    def create():
        pass


class PumpkinToffeeFactory(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Halloween"
        lactose = False
        nuts = True
        return Candy(theme, lactose, nuts, **kwargs)


class CandyCaneFactory(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Christmas"
        lactose = False
        nuts = False
        return Candy(theme, lactose, nuts, **kwargs)


class CremeEggsFactory(CandyFactory):
    @staticmethod
    def create(**kwargs):
        theme = "Easter"
        number = 1
        return Candy(theme, number, **kwargs)

