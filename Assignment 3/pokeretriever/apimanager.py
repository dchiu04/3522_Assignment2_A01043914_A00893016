
from aiohttp import ClientSession
import asyncio
from pokeretriever.retriever import Request


class APIManager:
    """
        Manages the JSON request calls to the pokeapi website.
    """

    def create_urls(self, request: Request):
        """

        :param request:
        :return:
        """

        urls = []
        for r in request.searches:
            urls.append("https://pokeapi.co/api/v2/" + request.mode + "/" + r)
        return urls

    async def get_json(self, url, session):
        """
            Gets the json request.
        :param url:
        :param session:
        :return:
        """
        response = await session.request(method="GET", url=url)
        if response.status == 200:
            try:
                return await response.json()
            except ValueError as e:
                print(e)
        return None

    async def manage_request(self, request):
        """

        :param request:
        :return:
        """
        urls = self.create_urls(request)
        calls = []
        results = []
        async with ClientSession() as session:
            for url in urls:
                calls.append(asyncio.create_task(self.get_json(url, session)))
                results = await asyncio.gather(*calls)
            return results




