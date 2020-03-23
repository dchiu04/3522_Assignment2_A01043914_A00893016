import abc
from candy import Candy, PumpkinToffee, CandyCane, CremeEggs


class CandyFactory(abc.ABC):
    """
        Base candy factory that all candy factories inherit from.
    """
    @abc.abstractmethod
    def create(self, **kwargs):
        pass


class PumpkinToffeeFactory(CandyFactory):
    """
        Halloween themed candy factory that makes candy.
    """
    def create(self, variety="", **kwargs):
        return PumpkinToffee(variety, **kwargs)


class CandyCaneFactory(CandyFactory):
    """
        Christmas themed candy factory that makes candy.
    """
    def create(self, colour="", **kwargs):
        return CandyCane(colour, **kwargs)


class CremeEggsFactory(CandyFactory):
    """
        Easter themed candy factory that makes candy.
    """
    def create(self, pack_size="",**kwargs):
        return CremeEggs(pack_size,**kwargs)
