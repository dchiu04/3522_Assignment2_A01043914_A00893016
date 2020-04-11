from urllib.request import Request
from argparse import ArgumentParser

from pokeretriever.apimanager import APIManager
from pokeretriever.pokeobject import PokemonStat, PokemonAbility, PokemonMove, Pokemon, Stats


class Request:
    def __init__(self, mode, input, output, is_expanded=False):
        self.mode = mode
        self.input = input
        self.is_expanded = is_expanded
        self.output = output
        self.searches = []

    def __str__(self):
        return f"Mode: {self.mode}\n" \
               f"Input: {self.input}\n" \
               f"Is Expanded: {self.is_expanded}\n" \
               f"Output Path: {self.output}\n"


class RequestManager:

    @staticmethod
    def parse_arguments_to_request() -> Request:

        parser = ArgumentParser()
        parser.add_argument("mode", help="It can be one of 3 specific modes, Pokemon, Ability, or Move.")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--inputfile", help="When providing a file name, the --inputfile flag "
                                               "must be provided.")
        group.add_argument("--inputdata", help="Either an id or a name. ")
        parser.add_argument("--expanded", help="")
        parser.add_argument("--output", help="")

        try:
            args = parser.parse_args()
            if args.inputfile:
                request = Request(args.mode.lower(), args.inputfile, args.expanded, args.output)
            else:
                request = Request(args.mode.lower(), args.inputdata, args.expanded, args.output)
            r = RequestManager.check_input(request)
            return r
        except Exception as e:
            print(e)

    @staticmethod
    def check_input(request):
        if request.input.endswith(".txt"):
            with open(request.input, 'r') as file:
                for line in file.readlines():
                    request.searches.append(line.rstrip('\n'))
        else:
            request.searches.append(request.input)
        return request


class RequestHandler:

    async def handle_request(self, request):
        api = APIManager()
        jsons = await api.manage_request(request)

        if request.mode == 'pokemon':
            for j in jsons:
                # poke = self._get_pokemon(j)
                print(self.get_pokemon(j))

        elif request.mode == 'ability':
            for j in jsons:
                print(self.get_ability(j))

        elif request.mode == 'move':
            for j in jsons:
                print(self.get_move(j))

    def get_pokemon(self, json):
        pName = json["name"]
        pId = int(json["id"])
        tempList = []
        height = int(json["height"])
        weight = int(json["weight"])
        for data in json["stats"]:
            tempid = int((data['stat']['url']).split('/')[6])
            temp = PokemonStat((data['stat']['name']), tempid, int((data['base_stat'])), (data['stat']['url']))
            tempList.append(temp)
        stats = Stats(tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5])
        types = []
        for data in json["types"]:
            temp = data['type']['name']
            types.append(temp)
        abilities = []
        for data in json["abilities"]:
            tempid = int((data['ability']['url']).split('/')[6])
            temp = PokemonAbility((data['ability']['name']), tempid, (data['ability']['url']))
            abilities.append(temp)
        moves = []
        for i in range(len(json["moves"])):
            name = json["moves"][i]["move"]["name"]
            level = int(json["moves"][i]["version_group_details"][0]["level_learned_at"])
            url = json["moves"][i]["move"]["url"]
            temp = PokemonMove(name, i + 1, level, url)
            moves.append(temp)
        return Pokemon(pName, pId, height, weight, stats, types, abilities, moves)

    def get_move(self, json):
        move = PokemonMove(json["name"], json["id"], 0, json["generation"]["name"],
                           json["accuracy"], json["pp"], json["power"],
                           json["type"]["name"], json["damage_class"]["name"],
                           json["effect_entries"][0]["short_effect"])
        return move

    def get_ability(self, json):
        pokelist = json["pokemon"]
        templist = []
        for poke in pokelist:
            templist.append(poke['pokemon']['name'])

        ability = PokemonAbility(json["name"], json["id"],
                                 json["generation"]["name"],
                                 json["effect_entries"][0]["effect"],
                                 json["effect_entries"][0]["short_effect"],
                                 templist)
        return ability
