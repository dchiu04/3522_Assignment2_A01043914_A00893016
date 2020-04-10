from pokeretriever.pokeobject import PokedexObject
from pokeretriever.retriever import Request, RequestManager
from pokeretriever.retriever import RequestHandler


class Pokedex:
    """
    Driver class that sets up chains of responsiblity.
    """

    def __init__(self):
        pass

    @staticmethod
    def execute_request(request: Request) -> PokedexObject:
        RequestHandler.handle_request(request)

def main():
    request = RequestManager.parse_arguments_to_request()
    pokedex = Pokedex()
    pokedex.execute_request(request)


if __name__ == "__main__":
    main()
