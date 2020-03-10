
class Animal:
    def __init__(self, stuffing, size, fabric, name, desc, prod_id):
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
        self._name = name
        self._desc = desc
        self._prod_id = prod_id

    @property
    def stuffing(self):
        return self._stuffing

    @property
    def size(self):
        return self._size

    @property
    def fabric(self):
        return self._fabric

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def prod_id(self):
        return self._prod_id

