import abc

from toy import SantaWorkshop, Spider, RobotBunny


class ToyFactory(abc.ABC):
    """
        Base toy factory that all toy factories inherit from.
    """
    @abc.abstractmethod
    def create(self, **kwargs):
        pass


class SantaWorkshopFactory(ToyFactory):
    """
        Christmas themed factory to make toys.
    """
    def create(self, dimensions="", num_rooms="", **kwargs):
        return SantaWorkshop(dimensions, num_rooms, **kwargs)


class SpiderFactory(ToyFactory):
    """
        Halloween themed factory to make toys.
    """
    def create(self, speed="", jump="", glow="", species="", **kwargs):
        return Spider(speed, jump, glow, species, **kwargs)


class RobotBunnyFactory(ToyFactory):
    """
        Easter themed factory to make toys.
    """
    def create(self, num_sound="", colour="", **kwargs):
        return RobotBunny(num_sound, colour, **kwargs)
