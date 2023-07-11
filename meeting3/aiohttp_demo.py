import asyncio
import time
from asyncio import TaskGroup

import aiohttp

url = "https://api.kanye.rest/"


async def get_quote(session):
    async with session.get(url, ssl=False) as resp:
        response = await resp.json()
        return response


async def main():
    s = time.time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with TaskGroup() as tg:
            for i in range(10):
                tasks.append(tg.create_task(get_quote(session)))
                # resp = await get_quote(session)
                # print(resp)
            # print(type(tasks[0]))
    # for completed_task in tasks:
    #     print(completed_task)
    e = time.time()
    print(f"Total: {e-s} seconds")

    for t in tasks:
        print(t.result())
asyncio.run(main(), debug=True)