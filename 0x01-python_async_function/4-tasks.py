#!/usr/bin/env python3
'''recreation of task 1'''
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    ''''using asyncio.Task'''
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [(await task) for task in asyncio.as_completed(tasks)]