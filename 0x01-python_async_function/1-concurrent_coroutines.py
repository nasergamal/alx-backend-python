#!/usr/bin/env python3
'''concurrent random async'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''group wait random'''
    tasks = [wait_random(max_delay) for i in range(n)]
    return [(await task) for task in asyncio.as_completed(tasks)]
