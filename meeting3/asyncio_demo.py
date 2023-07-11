import asyncio
import time
from asyncio import TaskGroup


async def wait(sec):
    print(f'Going to wait for {sec} seconds')
    await asyncio.sleep(sec)
    # time.sleep(sec)
    print(f'Finished waiting {sec} seconds')

# event loop:  wait(3)
# coroutine
async def main():
    # tasks = []
    async with TaskGroup() as tg:
        # for i in range(1, 6):
        #     tasks.append(tg.create_task(wait(i)))
        tasks = [tg.create_task(wait(i)) for i in range(1, 6)]

    print('Bye bye')


    # task1 = asyncio.create_task(wait(2))
    # task2 = asyncio.create_task(wait(3))

    # await asyncio.gather(task1, task2)
    # await task1
    # await task2
    #Going to wait for 2 seconds

if __name__ == '__main__':
    asyncio.run(main())
# asyncio.
# while True:


# r = main(2)
# executor.submit(main, 2)
# print(r)
# submit

# Eventloop
# while True:
#   is there a code to run
# print('Hello')
# ok, you can give the controal