class Order:
    def __init__(self, order_num, prod_id, item_type, name, prod_details, factory):
        self._order_num = order_num
        self._prod_id = prod_id
        self._item_type = item_type
        self._name = name
        self._prod_details = prod_details
        self._factory = factory

    @property
    def order(self):
        return self._order_num

    @property
    def type(self):
        return self._item_type

    @property
    def prod_id(self):
        return self._prod_id

    @property
    def name(self):
        return self._name

    @property
    def details(self):
        return self._prod_details

    @property
    def factory(self):
        return self._factory

    def __str__(self):
        return "Order: {}, Item {}, Product ID {}, Name ""{}"", Quantity {}" \
            .format(self.order(), self.type(), self.prod_id(),
                    self.name(), 100)
