import aiohttp
import asyncio
import time

start_time = time.time()

url = "https://api.kanye.rest/"
async def main():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 10):
            async with session.get(url, ssl=False) as resp:
                data = await resp.json()
                print(data)
# asyncio.gather()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))