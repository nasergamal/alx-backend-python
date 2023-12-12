#!/usr/bin/env python3
'''A try at async comprehension'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    run async_generator function which loops 10 times and returns
    a random number each time in an async comprehension
    '''
    return [num async for num in async_generator()]
