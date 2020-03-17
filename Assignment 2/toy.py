import abc


class Toy(abc.ABC):
    def _init_(self, battery, min_age, name, desc, prod_id):
        self.battery = battery
        self.min_age = min_age
        self.name = name
        self.desc = desc
        self.prod_id = prod_id


class SantaWorkshop(Toy):
    def _init_(self, dimensions, num_rooms, **kwargs):
        super()._init_(kwargs.get("battery"),
                       kwargs.get("min_age"),
                       kwargs.get("name"),
                       kwargs.get("desc"),
                       kwargs.get("prod_id"))
        self.dimensions = dimensions
        self.num_rooms = num_rooms


class Spider(Toy):
    def _init_(self, speed, jump, glow, species, **kwargs):
        super()._init_(kwargs.get("battery"),
                       kwargs.get("min_age"),
                       kwargs.get("name"),
                       kwargs.get("desc"),
                       kwargs.get("prod_id"))
        self.speed = speed
        self.jump = jump
        self.glow = glow
        self.species = species


class RobotBunny(Toy):
    def _init_(self, num_sound_effect, color, **kwargs):
        super()._init_(kwargs.get("battery"),
                       kwargs.get("min_age"),
                       kwargs.get("name"),
                       kwargs.get("desc"),
                       kwargs.get("prod_id"))
        self.num_sound_effect = num_sound_effect
        self.color = color
