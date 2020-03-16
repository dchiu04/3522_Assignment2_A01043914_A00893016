import abc
from candy import Candy


class CandyFactory(abc.ABC):
    @staticmethod
    def create(has_nuts, has_lactose, name, description, product_id):
        pass


class PumpkinToffeeFactory(CandyFactory):
    @staticmethod
    def create(has_lactose, has_nuts, **kwargs):
        theme = "Halloween"
        lactose = has_lactose
        nuts = has_nuts
        return Candy(theme, lactose, nuts, **kwargs)


class CandyCaneFactory(CandyFactory):
    @staticmethod
    def create(has_lactose, has_nuts, **kwargs):
        theme = "Christmas"
        lactose = has_lactose
        nuts = has_nuts
        return Candy(theme, lactose, nuts, **kwargs)


class CremeEggsFactory(CandyFactory):
    @staticmethod
    def create(has_lactose, has_nuts, size, **kwargs):
        theme = "Easter"
        lactose = has_lactose
        nuts = has_nuts
        number = size
        return Candy(theme, lactose, nuts, number, **kwargs)
