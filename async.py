import asyncio
import time


async def func1():
    time.sleep(2)
    print("Function 1 calling")


async def func2():
    print("Function 2 calling")


async def main():
    asyncio.gather(func1(), func2())

asyncio.run(main())
