class Candy:
    def __init__(self, quantity, nuts, lactose, name, desc, prod_id):
        self._quantity = quantity
        self._nuts = nuts
        self._lactose = lactose
        self._name = name
        self._desc = desc
        self._prod_id = prod_id


class PumpkinToffee(Candy):
    def __init__(self, variety, **kwargs):
        super().__init__(kwargs.get("quantity"),
                         kwargs.get("nuts"),
                         kwargs.get("lactose"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("prod_id")
                         )
        self._variety = variety


class CandyCane(Candy):
    def __init__(self, colour, **kwargs):
        super().__init__(kwargs.get("quantity"),
                         kwargs.get("nuts"),
                         kwargs.get("lactose"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("prod_id")
                         )
        self._colour = colour


class CremeEggs(Candy):
    def __init__(self, pack_size, **kwargs):
        super().__init__(kwargs.get("quantity"),
                         kwargs.get("nuts"),
                         kwargs.get("lactose"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("prod_id")
                         )
        self._pack_size = pack_size
