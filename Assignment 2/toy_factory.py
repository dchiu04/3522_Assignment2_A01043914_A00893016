import abc

from toy import Toy


class ToyFactory(abc.Abc):
    @staticmethod
    def create(battery, min_age, name, desc, prod_id):
        pass


class SantaFactory(ToyFactory):
    @staticmethod
    def create(width, height, num_rooms, **kwargs):
        battery = False
        w = width
        h = height
        rooms = num_rooms
        #return Toy(battery, w, h, rooms)


class RCSpider(ToyFactory):
    @staticmethod
    def create(speed, jump, glow, spider_type, **kwargs):
        sp = speed
        j_height = jump
        g = glow
        sp_type = spider_type
        #return Toy(sp, j_height, g, sp_type)


class RobotBunny(ToyFactory):
    @staticmethod
    def create(num_effects, color, **kwargs):
        battery = True
        sound = num_effects
        col = color
        #return Toy(battery, sound, col)
