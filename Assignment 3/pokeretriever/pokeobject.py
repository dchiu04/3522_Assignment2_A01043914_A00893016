from abc import ABC


class PokedexObject(ABC):
    def __init__(self, name, id):
        self._name = name
        self._id = id


class Pokemon(PokedexObject):
    def __init__(self, name, id, height, weight, stats, types, abilities, moves):
        super().__init__(name, id)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def stats(self):
        return self._stats

    @property
    def types(self):
        return self._types

    @property
    def abilities(self):
        return self._abilities

    @property
    def moves(self):
        return self._moves

    def __str__(self):
        return f"name: {self._name}\n" \
               f"id: {self._id}\n" \
               f"Height: {self._height}\n" \
               f"Weight: {self._weight}\n"


class PokemonAbility(PokedexObject):
    def __init__(self, name, id, url=None, generation=None, effect=None, effect_short=None, pokemon=[]):
        super().__init__(name, id)
        self._url = url
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
        return f"name: {self._name}\n" \
               f"id: {self._id}\n" \
               f"effect: {self._effect}\n"


class Stats:
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
        return f"Stats:\n" \
               f"Speed: {self._speed}\n" \
               f"Special Defense: {self._sp_def}\n" \
               f"Special Attack: {self._sp_atk}\n"


class PokemonStat(PokedexObject):
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

    def __str__(self):
        return f"name: {self._name}\n" \
               f"id: {self._id}\n" \
               f"base_value: {self._base_value}\n" \
               f"url: {self._url}\n"


class PokemonMove(PokedexObject):
    def __init__(self, name, id, level=None, url=None, generation=None, accuracy=None, pp=None, power=None, type=None,
                 damage_class=None, effect_short=None):
        super().__init__(name, id)
        self._level = level
        self._url = url
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
        return f"name: {self._name}\n" \
               f"id: {self._id}\n" \
               f"level: {self._level}\n" \
               f"url: {self._url}\n"
