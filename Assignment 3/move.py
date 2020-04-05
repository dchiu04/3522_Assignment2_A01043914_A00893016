class Move:
    def __init__(self, name, id, generation, accuracy, pp, power, type, damage_class, effect_short):
        self._name = name
        self._id = id
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self.power = power
        self._type = type
        self._damage_class = damage_class
        self._effect_short = effect_short

