from urllib.request import Request


# Need a better name for this class (refactor -> rename)
class PokedexObject(object):
    pass


class Facade:
    def execute_request(self, request: Request) -> PokedexObject:
        pass
