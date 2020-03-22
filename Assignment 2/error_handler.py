class BatteryException(Exception):
    """
    If an order's constructor is passed in parameters for a toy that is intended to require
    or not require batteries but is told to make an order of the opposite, this
    exception should be thrown. Moreover, if this is N or F, this should be thrown.
    """

    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Has Batteries can only be ""Y"" or ""N""\n"
        file.write(string.format(k._order_num, Exception))


class MinAgeException(Exception):
    """
    If an order is passed in parameters for a toy that has a fixed minimum age
    then this exception should be thrown. Moreover, if a non-integer value is
    passed in as a minimum age, this should be thrown.
    """

    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Min Age can only be an integer.\n"
        file.write(string.format(k._order_num, Exception))


class SpiderTypeException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Spider type can only be ""Wolf Spider"" or ""Tarantula""\n"
        file.write(string.format(k._order_num, Exception))


class AnimalColourException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Animal colour can only be ""White"" or ""Grey"" \
                 or ""Pink"" or ""Blue""\n"
        file.write(string.format(k._order_num, Exception))



class ToyColourException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Toy colour can only be ""Orange"" or ""Blue" \
                 "or ""Pink""\n"
        file.write(string.format(k._order_num, Exception))


class CandyColourException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Candy colour can only be ""Red"" or ""Green""\n"
        file.write(string.format(k._order_num, Exception))


class HasLactoseException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - HasLactose can only be ""Y"" or ""N""\n"
        file.write(string.format(k._order_num, Exception))


class HasNutsException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - HasNuts can only be ""Y"" or ""N""\n"
        file.write(string.format(k._order_num, Exception))


class VarietyException(Exception):
    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Variety can only be ""Sea Salt"" or ""Regular""\n"
        file.write(string.format(k._order_num, Exception))


class StuffingException(Exception):
    """
    If a stuffing is requested that doesn't match a specific stuffed animal's
    this exception should be thrown. It should also be thrown if an invalid
    stuffing is expected.
    """

    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Stuffing can only be ""Polyester Fibrefill"" or ""Wool""\n"
        file.write(string.format(k._order_num, Exception))


class SizeException(Exception):
    """
    If a size is requested that doesn't match a specific stuffed animal's
    this exception should be thrown. It should also be thrown if an invalid
    fabric is expected.
    """

    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Size can only be ""S"" or ""M"" \
                 or ""L""\n"
        file.write(string.format(k._order_num, Exception))


class FabricException(Exception):
    """
    If a fabric is requested that doesn't match a specific stuffed animal's
    this exception should be thrown. It should also be thrown if an invalid
    fabric is expected.
    """

    def __init__(self, file, k):
        string = "Order: {}, Could be process order data was corrupted," \
                 " {} - Fabric can only be ""Linen"" or ""Acrylic"" \
                 or ""Cotton""\n"
        file.write(string.format(k._order_num, Exception))


battery = {'Halloween': {'Y': True},
           'Christmas': {'N': True},
           'Easter': {'Y': True}}

# Questionable
has_glow = {'Halloween': {'Y': True}}

spider_type = {'Halloween': {'Tarantula': True, 'Wolf Spider': True}}

toy_colour = {'Easter': {'Orange': True, 'Blue': True, 'Pink': True}}

stuff_animal_colour = {'Easter': {'White': True, 'Grey': True, 'Pink': True, 'Blue': True}}

candy_colour = {'Christmas': {'Red': True, 'Green': True}}

has_lactose = {'Halloween': {'Y': True},
               'Christmas': {'N': True},
               'Easter': {'Y': True}}

has_nuts = {'Halloween': {'Y': True},
            'Christmas': {'N': True},
            'Easter': {'Y': True}}

variety = {'Halloween': {'Sea Salt': True, 'Regular': True}}

stuffing = {'Halloween': {'Polyester Fibrefill': True},
            'Christmas': {'Wool': True},
            'Easter': {'Polyester Fibrefill': True}}

size = {'Halloween': {'S': True, 'M': True, 'L': True},
        'Christmas': {'S': True, 'M': True, 'L': True},
        'Easter': {'S': True, 'M': True, 'L': True}}

fabric = {'Halloween': {'Acrylic': True},
          'Christmas': {'Cotton': True},
          'Easter': {'Linen': True}}


class ErrorHandler:
    """
    This class checks arguments to see if they are valid or not.
    """

    @staticmethod
    def error_check(holiday, item, **kwargs):
        if item == "Toy":
            try:
                battery[holiday][kwargs.get("has_batteries")]
                return True
            except KeyError:
                raise BatteryException
        elif item == "Stuffed Animal":
            try:
                stuffing[holiday][kwargs.get("stuffing")]
                return True
            except KeyError:
                raise StuffingException
            try:
                fabric[holiday][kwargs.get("fabric")]
                return True
            except KeyError:
                raise FabricException
        elif item == "Candy":
            pass
        return False
