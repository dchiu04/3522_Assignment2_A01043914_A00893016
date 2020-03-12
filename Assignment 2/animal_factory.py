import abc
from animal import Animal

class AnimalFactory(abc.Abc):
    @staticmethod
    def create(stuffing, size, fabric, name, desc, prod_id):
        pass

class SkeletonFactory(AnimalFactory):
    @staticmethod
    def create(**kwargs):
        yarn = "Acrylic Yarn"
        glow_in_dark = True
        #return Animal(yarn, glow_in_dark)

class ReindeerFactory(AnimalFactory):
    @staticmethod
    def create(**kwargs):
        stuffing = "Wool"
        fabric = "Cotton"
        glow = True
        #return Animal(stuffing, fabric, glow)

class BunnyFactory(AnimalFactory):
    @staticmethod
    def create(col, **kwargs):
        stuffing = "Polyester Fiberfill"
        fabric = "Linen"
        colours = col
        #return Animal(stuffing, fabric, colours)