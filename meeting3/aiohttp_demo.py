import asyncio
import time
from asyncio import TaskGroup

import aiohttp

url = "https://api.kanye.rest/"

quotes = []


async def get_quote(session):
    async with session.get(url, ssl=False) as resp:
        # curr_list_len = len(quotes)
        response = await resp.json()
        # print(curr_list_len, '==', len(quotes))
        # quotes.append(response)
        return response

# async def main():
#     s = time.time()
#     quotes = []
#     async with aiohttp.ClientSession() as session:
#         for i in range(100):
#             result = await asyncio.create_task(get_quote(session))
#             quotes.append(result)
#     e = time.time()
#     print(f"Total: {e-s} seconds")
#
#     print(quotes)

async def main():
    s = time.time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with TaskGroup() as tg:
            for i in range(100):
                tasks.append(tg.create_task(get_quote(session)))
        # I reach this only when all the taskss are finished
    e = time.time()
    print(f"Total: {e-s} seconds")

    print(quotes)

    # for t in tasks:
    #     print(t.result())
        # print(t)
asyncio.run(main(), debug=True)
