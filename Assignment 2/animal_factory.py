import abc
from animal import Animal, Skeleton, Bunny, Reindeer


class AnimalFactory(abc.ABC):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass


class SkeletonFactory(AnimalFactory):
    def create(self, has_glow="", **kwargs):
        return Skeleton(has_glow, **kwargs)


class ReindeerFactory(AnimalFactory):
    def create(self, has_glow="", **kwargs):
        return Reindeer(has_glow, **kwargs)


class BunnyFactory(AnimalFactory):
    def create(self, colour="", **kwargs):
        return Bunny(colour, **kwargs)
