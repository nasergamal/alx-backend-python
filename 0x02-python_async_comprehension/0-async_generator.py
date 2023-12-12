#!/usr/bin/env python3
'''an async generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Returns a generator that loop ten times return a random
    number between 0 and 10 each time
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
