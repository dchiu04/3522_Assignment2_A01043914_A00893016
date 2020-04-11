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
        json_results = []
        sreuslt = []
        areuslt = []
        mreuslt = []
        async with ClientSession() as session:
            if len(request.stat_urls) > 0:
                for urls in request.stat_urls:
                    for url in urls:
                        calls.append(asyncio.create_task(self.get_json(url, session)))
                        results += await asyncio.gather(*calls)
                        sreuslt.append(results)
                        calls = []
                        results = []
                json_results.append(sreuslt)

                for urls in request.ability_urls:
                    for url in urls:
                        calls.append(asyncio.create_task(self.get_json(url, session)))
                        results += await asyncio.gather(*calls)
                        areuslt.append(results)
                        calls = []
                        results = []
                json_results.append(areuslt)

                for urls in request.move_urls:
                    for url in urls:
                        calls.append(asyncio.create_task(self.get_json(url, session)))
                        results += await asyncio.gather(*calls)
                        mreuslt.append(results)
                        calls = []
                        results = []
                json_results.append(mreuslt)

            else:
                for url in urls:
                    calls.append(asyncio.create_task(self.get_json(url, session)))
                    json_results = await asyncio.gather(*calls)

            return json_results
