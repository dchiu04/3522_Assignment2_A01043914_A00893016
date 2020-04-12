from abc import ABC


class PokedexObject(ABC):
    """
        Pokemon object that exists in the pokedex
    """

    def __init__(self, name, id):
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id


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

    @property
    def types(self):
        return self._types

    def __str__(self):

        # Requires additional formatting to make it look nice
        types = ""
        count = 1
        for type in self._types:
            types = types + "    Type " + str(count) + ": " + type.title() + "\n"
            count = count + 1

        abilities = ""
        count = 1
        for ability in self._abilities:
            abilities = abilities + "    Ability " + str(count) + ": " + ability._name.title() + "\n"
            count = count + 1

        moves = ""
        count = 1
        for move in self._moves:
            moves = moves + "    Move " + str(count) + ": " + move._name.title() + " (Learned at level: " + str(
                move.level) + ")\n"
            count = count + 1

        return f"Name: {self._name.title()}\n" \
               f"Id: {self._id}\n" \
               f"Height: {self._height} decimeters\n" \
               f"Weight: {self._weight} hectograms\n" \
               f"Stats:{self._stats}" \
               f"Type(s):\n{types}" \
               f"Ability(s):\n{abilities}" \
               f"Moves(s):\n{moves}"


class PokemonAbility(PokedexObject):
    """
        Each Pokemon's individual abilities and their context.
    """

    def __init__(self, name, id, generation=None, effect=None, effect_short=None, pokemon=None):
        super().__init__(name, id)
        if pokemon is None:
            pokemon = []
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    @property
    def generation(self):
        return self._generation

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

        # Requires additional formatting to make it look nice
        pokes = ""
        count = 1

        for pokemons in self.pokemon:
            pokes += "    Pokemon " + str(count) + ": " + pokemons.title() + "\n"
            count = count + 1

        effects = ""
        for eff in self.effect:
            if eff == "\n":
                continue
            if eff == ".":
                effects += eff + " "
                continue
            effects += eff


        return f"Name: {self._name.title()}\n" \
               f"Id: {self._id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {effects}\n" \
               f"Effect (short): {self.effect_short}\n" \
               f"Pokemon:\n{pokes}"


class Stats:
    """
        Determines the individual pokemon's stats.
    """

    def __init__(self, speed=None, sp_def=None, sp_atk=None, defense=None, attack=None, hp=None):
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
        return f"\n    Speed: {self._speed.base_value}\n" \
               f"    Special Defense: {self._sp_def.base_value}\n" \
               f"    Special Attack: {self._sp_atk.base_value}\n" \
               f"    Defense: {self._defense.base_value}\n" \
               f"    Attack: {self._attack.base_value}\n" \
               f"    HP: {self._hp.base_value}\n"


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

    def __str__(self):
        return f"Name: {self._name}\n" \
               f"Id: {self._id}\n" \
               f"Base_Value: {self._base_value}\n" \
               f"Url: {self._url}\n"


class PokemonMove(PokedexObject):
    """
        Individual pokemon's ability and their stats.
    """

    def __init__(self, name, id, level=None, generation=None, accuracy=None, pp=None, power=None, type=None,
                 damage_class=None, effect_short=None, url=None):
        super().__init__(name, id)
        self._level = level
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type
        self._damage_class = damage_class
        self._effect_short = effect_short
        self._url = url

    @property
    def level(self):
        return self._level

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
               f"Effect (short): {self._effect_short}\n"
