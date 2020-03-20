class Animal:
    def __init__(self, stuffing, size, fabric, name, desc, prod_id):
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
        self._name = name
        self._desc = desc
        self._prod_id = prod_id


class Skeleton(Animal):
    def __init__(self, has_glow, **kwargs):
        super().__init__(
                         kwargs.get("stuffing"),
                         kwargs.get("size"),
                         kwargs.get("fabric"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("prod_id")
                         )
        self._has_glow = has_glow


class Reindeer(Animal):
    def __init__(self, has_glow, **kwargs):
        super().__init__(
                         kwargs.get("stuffing"),
                         kwargs.get("size"),
                         kwargs.get("fabric"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("prod_id")
                         )
        self._has_glow = has_glow


class Bunny(Animal):
    def __init__(self, colour, **kwargs):
        super().__init__(
                         kwargs.get("stuffing"),
                         kwargs.get("size"),
                         kwargs.get("fabric"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("prod_id")
                         )
        self._colour = colour
