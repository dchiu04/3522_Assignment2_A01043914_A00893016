import abc


class ToyFactory(abc.Abc):
    @staticmethod
    def create(battery, min_age, name, desc, prod_id):
        pass


class SantaFactory(ToyFactory):

    @staticmethod
    def create(width, height, num_rooms, **kwargs):
        pass


class RCSpider(ToyFactory):
    @staticmethod
    def create(speed, jump, glow, spider_type, **kwargs):
        pass


class RobotBunny(ToyFactory):
    @staticmethod
    def create(num_effects, color, **kwargs):
        pass
