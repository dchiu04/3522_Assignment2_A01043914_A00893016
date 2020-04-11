from abc import ABC


class PokedexObject(ABC):
    """
        Pokemon object that exists in the pokedex
    """

    def __init__(self, name, id):
        self._name = name
        self._id = id


class Pokemon(PokedexObject):
    """
        Individual pokemon object with its own stats.
    """

    def __init__(self, name, id, height, weight, stats, types, abilities, moves):
        super().__init__(name, id)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    @property
    def stats(self):
        return self._stats

    @property
    def abilities(self):
        return self._abilities

    @property
    def moves(self):
        return self._moves

    def types(self):
        return self._types

    def __str__(self):
        """
        Formatted string for Pokemon object.
        :return: str
        """

        return f"Name: {self._name.title()}\n" \
                f"Id: {self._id}\n" \
                f"Height: {self._height} decimeters\n" \
                f"Weight: {self._weight} hectograms\n" \
                f"Stats: {self._stats}\n" \
                f"Type(s): {self._types}\n" \
                f"Ability(s): {self._abilities}\n" \
                f"Move(s): {self._moves}\n"


class PokemonAbility(PokedexObject):
    """
        Each Pokemon's individual abilities and their context.
    """

    def __init__(self, name, id, generation=None, effect=None, effect_short=None, pokemon=[]):
        super().__init__(name, id)
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    @property
    def generation(self):
        return self.generation

    @property
    def effect(self):
        return self._effect

    @property
    def effect_short(self):
        return self._effect_short

    @property
    def pokemon(self):
        return self._pokemon

    def __str__(self):
        return f"Name: {self._name.title()}\n" \
               f"Id: {self._id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect (short): {self.effect_short}\n" \
               f"Pokemon:\n    {self._pokemon}"


class Stats:
    """
        Determines the individual pokemon's stats.
    """

    def __init__(self, speed, sp_def, sp_atk, defense, attack, hp):
        self._speed = speed
        self._sp_def = sp_def
        self._sp_atk = sp_atk
        self._defense = defense
        self._attack = attack
        self._hp = hp

    @property
    def speed(self):
        return self._speed

    @property
    def sp_def(self):
        return self._sp_def

    @property
    def sp_atk(self):
        return self._sp_atk

    @property
    def defense(self):
        return self._defense

    @property
    def attack(self):
        return self._attack

    @property
    def hp(self):
        return self._hp

    def __str__(self):
        return f"\n    Speed: {self._speed}\n" \
               f"    Special Defense: {self._sp_def}\n" \
               f"    Special Attack: {self._sp_atk}\n" \
               f"    Defense: {self._defense}\n" \
               f"    Attack: {self._attack}\n" \
               f"    HP: {self._hp}\n"


class PokemonStat(PokedexObject):
    """
        Categorizes stats.
    """

    def __init__(self, name, id, base_value=None, url=None, is_battle_only=None):
        super().__init__(name, id)
        self._url = url
        self._base_value = base_value
        self._is_battle_only = is_battle_only

    @property
    def is_battle_only(self):
        return self._is_battle_only

    @property
    def base_value(self):
        return self._base_value

    # def __str__(self):
    #     return f"Name: {self._name}\n" \
    #            f"Id: {self._id}\n" \
    #            f"Base_Value: {self._base_value}\n" \
    #            f"Url: {self._url}\n"


class PokemonMove(PokedexObject):
    """
        Individual pokemon's ability and their stats.
    """

    def __init__(self, name, id, generation=None, accuracy=None, pp=None, power=None, type=None,
                 damage_class=None, effect_short=None):
        super().__init__(name, id)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type
        self._damage_class = damage_class
        self._effect_short = effect_short

    @property
    def generation(self):
        return self._generation

    @property
    def accuracy(self):
        return self._accuracy

    @property
    def pp(self):
        return self._pp

    @property
    def power(self):
        return self._power

    @property
    def type(self):
        return self._type

    @property
    def damage_class(self):
        return self._damage_class

    @property
    def effect_short(self):
        return self._effect_short

    def __str__(self):
        return f"Name: {self._name.title()}\n" \
               f"Id: {self._id}\n" \
               f"Generation: {self._generation}\n" \
               f"Accuracy: {self._accuracy}\n" \
               f"PP: {self._pp}\n" \
               f"Power: {self._power}\n" \
               f"Type: {self._type}\n" \
               f"Damage Class: {self._damage_class}\n" \
               f"Effect (short): {self._effect_short}"
