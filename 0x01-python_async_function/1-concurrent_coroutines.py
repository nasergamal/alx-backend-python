#!/usr/bin/env python3
'''concurrent random async'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''group wait random'''
    tasks = [wait_random(max_delay) for i in range(n)]
    return [(await task) for task in asyncio.as_completed(tasks)]
