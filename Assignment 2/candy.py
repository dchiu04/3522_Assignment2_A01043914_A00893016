
class Candy:
    def __init__(self, nuts, lactose, name, desc, prod_id):
        self._nuts = nuts
        self._lactose = lactose
        self._name = name
        self._desc = desc
        self._prod_id = prod_id

    @property
    def nuts(self):
        return self._nuts

    @property
    def lactose(self):
        return self._lactose

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def prod_id(self):
        return self._prod_id

