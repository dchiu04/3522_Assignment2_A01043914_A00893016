import abc

from toy import Toy


class ToyFactory(abc.ABC):
    @abc.abstractmethod
    def create(self, battery, min_age, name, desc, prod_id):
        pass


class SantaFactory(ToyFactory):
    @staticmethod
    def create(dimensions, num_rooms, **kwargs):
        d = dimensions
        rooms = num_rooms
        return Toy(d, rooms, **kwargs)


class RCSpiderFactory(ToyFactory):
    @staticmethod
    def create(speed, jump, glow, spider_type, **kwargs):
        sp = speed
        j_height = jump
        g = glow
        sp_type = spider_type
        return Toy(sp, j_height, g, sp_type, **kwargs)


class RobotBunnyFactory(ToyFactory):
    @staticmethod
    def create(num_effects, color, **kwargs):
        battery = True
        sound = num_effects
        col = color
        return Toy(battery, sound, col, **kwargs)
