#!/usr/bin/env python3
'''measure runtime of for functions run concurrently using asyncio'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the time taken by four concurrent functions, each
    requiring 10 seconds to finish
    '''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.perf_counter() - start
