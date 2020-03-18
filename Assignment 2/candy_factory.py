import abc
from candy import Candy, PumpkinToffee, CandyCane, CremeEggs


class CandyFactory(abc.ABC):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass


class PumpkinToffeeFactory(CandyFactory):
    def create(self, variety="", **kwargs):
        return PumpkinToffee(variety, **kwargs)


class CandyCaneFactory(CandyFactory):
    def create(self, colour="", **kwargs):
        return CandyCane(colour, **kwargs)


class CremeEggsFactory(CandyFactory):
    def create(self, pack_size="",**kwargs):
        return CremeEggs(pack_size,**kwargs)
