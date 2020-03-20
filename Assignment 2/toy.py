import abc


class Toy(abc.ABC):
    def __init__(self, battery, min_age, name, desc, prod_id):
        self._battery = battery
        self._min_age = min_age
        self._name = name
        self._desc = desc
        self._prod_id = prod_id


class SantaWorkshop(Toy):
    def __init__(self, dimensions, num_rooms, **kwargs):
        super().__init__(
            kwargs.get("battery"),
            kwargs.get("min_age"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("prod_id")
        )
        self._dimensions = dimensions
        self._num_rooms = num_rooms


class Spider(Toy):
    def __init__(self, speed, jump, glow, species, **kwargs):
        super().__init__(
            kwargs.get("battery"),
            kwargs.get("min_age"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("prod_id")
        )
        self._speed = speed
        self._jump = jump
        self._glow = glow
        self._species = species


class RobotBunny(Toy):
    def __init__(self, num_sound, colour, **kwargs):
        super().__init__(
            kwargs.get("battery"),
            kwargs.get("min_age"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("prod_id")
        )
        self._num_sound = num_sound
        self._colour = colour
