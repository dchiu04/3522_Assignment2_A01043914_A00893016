import abc
from toy import SantaWorkshop
from toy import Spider
from toy import RobotBunny


class ToysFactory(abc.ABC):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass


class SantaWorkshopFactory(ToysFactory):
    def create(self, **kwargs):
        SantaWorkshop(**kwargs)


class SpiderFactory(ToysFactory):
    def create(self, **kwargs):
        Spider(**kwargs)


class RobotBunnyFactory(ToysFactory):
    def create(self, **kwargs):
        RobotBunny(**kwargs)