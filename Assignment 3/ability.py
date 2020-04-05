class Ability:
    def __init__(self, name, id, generation, effect, effect_short, pokemon):
        self._name = name
        self._id = id
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon
