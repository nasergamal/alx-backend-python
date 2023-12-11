#!/usr/bin/env python3
'''recreation of task 0'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    '''asyncio task'''
    return asyncio.Task(wait_random(max_delay))
