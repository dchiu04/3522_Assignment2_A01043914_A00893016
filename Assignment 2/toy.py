
class Toy:
    def __init__(self, has_batteries, min_age, name, desc, prod_id):
        self._has_batteries = has_batteries
        self._min_age = min_age
        self._name = name
        self._desc = desc
        self._prod_id = prod_id

    @property
    def has_batteries(self):
        return self._has_batteries

    @property
    def min_age(self):
        return self._min_age

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def prod_id(self):
        return self._prod_id

