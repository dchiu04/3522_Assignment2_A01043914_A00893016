from urllib.request import Request
from argparse import ArgumentParser

from pokeretriever.apimanager import APIManager
from pokeretriever.pokeobject import PokemonStat, PokemonAbility, PokemonMove, Pokemon, Stats


class Request:
    def __init__(self, mode, input, is_expanded, output):
        self.mode = mode
        self.input = input
        self.is_expanded = is_expanded
        self.output = output
        self.searches = []
        self.stat_urls = []
        self.ability_urls = []
        self.move_urls = []

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

        parser.add_argument("--expanded", action="store_true", help="")
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
        if request.is_expanded and request.mode == 'pokemon':
            stat_urls = []
            ability_urls = []
            move_urls = []
            pokemonlist = []
            for j in jsons:
                temppokemon = self.get_pokemon(j)
                pokemonlist.append(temppokemon)
                for i in range(len(j['stats'])):
                    stat_urls.append(j['stats'][i]['stat']['url'])
                for a in j['abilities']:
                    ability_urls.append(a['ability']['url'])
                for i in range(len(j['moves'])):
                    move_urls.append(j['moves'][i]['move']['url'])

                request.stat_urls.append(stat_urls)
                request.ability_urls.append(ability_urls)
                request.move_urls.append(move_urls)
                stat_urls = []
                ability_urls = []
                move_urls = []
            jsons = await api.manage_request(request)

            for pokemon in pokemonlist:
                pokemon.stats.speed.is_battle_only = (jsons[0][0][0]['is_battle_only'])
                pokemon.stats.sp_def.is_battle_only = (jsons[0][1][0]['is_battle_only'])
                pokemon.stats.sp_atk.is_battle_only = (jsons[0][2][0]['is_battle_only'])
                pokemon.stats.defense.is_battle_only = (jsons[0][3][0]['is_battle_only'])
                pokemon.stats.attack.is_battle_only = (jsons[0][4][0]['is_battle_only'])
                pokemon.stats.hp.is_battle_only = (jsons[0][5][0]['is_battle_only'])

            i = 0
            for pokemon in pokemonlist:
                tempabilities = []
                for ability in pokemon.abilities:
                    ability = self.get_ability(jsons[1][i][0])
                    tempabilities.append(ability)
                    i = i + 1
                pokemon.abilities = tempabilities

            i = 0
            for pokemon in pokemonlist:
                tempmoves = []
                for move in pokemon.moves:
                    move = self.get_move(jsons[2][i][0])
                    tempmoves.append(move)
                    i = i + 1
                pokemon.moves = tempmoves
                print(pokemon.moves[0])

        else:
            if request.mode == 'pokemon':
                for j in jsons:
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
            temp = PokemonStat((data['stat']['name']), tempid, int((data['base_stat'])))
            temp.url = (data['stat']['url'])
            tempList.append(temp)
        stats = Stats(tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5])
        types = []
        for data in json["types"]:
            temp = data['type']['name']
            types.append(temp)
        abilities = []
        for data in json["abilities"]:
            tempid = int((data['ability']['url']).split('/')[6])
            temp = PokemonAbility((data['ability']['name']), tempid)
            temp.url = (data['ability']['url'])
            abilities.append(temp)
        moves = []
        for i in range(len(json["moves"])):
            name = json["moves"][i]["move"]["name"]
            level = int(json["moves"][i]["version_group_details"][0]["level_learned_at"])
            temp = PokemonMove(name, i + 1, level)
            temp.url = json["moves"][i]["move"]["url"]
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
