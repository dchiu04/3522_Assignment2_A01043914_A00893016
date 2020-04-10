import requests

from pokeretriever.retriever import Request


class APIManager:

    def create_urls(self, request: Request):
        urls = []
        for r in request.searches:
            urls.append("https://pokeapi.co/api/v2/" + request.mode + "/" + r)
        print(urls)
        return urls

    def get_json(self, url):
        response = requests.get(url)
        return response.json()
