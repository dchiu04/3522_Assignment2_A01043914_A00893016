import abc

from toy import SantaWorkshop, Spider, RobotBunny


class ToyFactory(abc.ABC):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass


class SantaWorkshopFactory(ToyFactory):
    def create(self, dimensions="", num_rooms="", **kwargs):
        return SantaWorkshop(dimensions, num_rooms, **kwargs)


class SpiderFactory(ToyFactory):
    def create(self, speed="", jump="", glow="", species="", **kwargs):
        return Spider(speed, jump, glow, species, **kwargs)


class RobotBunnyFactory(ToyFactory):
    def create(self, num_sound="", colour="", **kwargs):
        return RobotBunny(num_sound, colour, **kwargs)
