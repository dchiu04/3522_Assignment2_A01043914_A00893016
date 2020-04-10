import requests
from aiohttp import ClientSession
import asyncio

from pokeretriever.retriever import Request


class APIManager:

    def create_urls(self, request: Request):
        urls = []
        for r in request.searches:
            urls.append("https://pokeapi.co/api/v2/" + request.mode + "/" + r)
        return urls

    async def get_json(self, url, session):
        response = await session.request(method="GET", url=url)
        if response.status == 200:
            try:
                return await response.json()
            except ValueError as e:
                print(e)
        return None

    async def manage_request(self, request):
        urls = self.create_urls(request)
        calls = []
        results = []
        async with ClientSession() as session:
            for url in urls:
                calls.append(asyncio.create_task(self.get_json(url, session)))
                results = await asyncio.gather(*calls)
            return results




