import abc
from animal import Animal

class AnimalFactory(abc.ABC):

    @staticmethod
    def create(stuffing, size, fabric, name, desc, product_id):
        pass


class SkeletonFactory(AnimalFactory):
    @staticmethod
    def create(fabric, stuffing, has_glow, **kwargs):
        yarn = fabric
        stuff = stuffing
        glow_in_dark = has_glow
        return Animal(yarn, stuff, glow_in_dark, **kwargs)


class ReindeerFactory(AnimalFactory):
    @staticmethod
    def create(fabric, stuffing, has_glow, **kwargs):
        stuff = stuffing
        yarn = fabric
        glow = has_glow
        return Animal(yarn, stuff, glow, **kwargs)


class BunnyFactory(AnimalFactory):
    @staticmethod
    def create(fabric, stuffing, colour, **kwargs):
        stuff = stuffing
        yarn = fabric
        colours = colour
        return Animal(stuffing, fabric, colours, **kwargs)
