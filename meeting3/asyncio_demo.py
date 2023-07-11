import asyncio
import time


async def wait(sec):
    print(f'Going to wait for {sec} seconds')
    await asyncio.sleep(sec)
    # time.sleep(sec)
    print(f'Finished waiting {sec} seconds')

# event loop:  wait(3)
# coroutine
async def main():

    task1 = asyncio.create_task(wait(2))
    task2 = asyncio.create_task(wait(3))

    await task1
    await task2
    #Going to wait for 2 seconds


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