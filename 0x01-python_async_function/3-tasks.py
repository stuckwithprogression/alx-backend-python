#!/usr/bin/env python3
'''asynchronous tasks
'''

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    '''takes in an integer argument and returns an asynchronous task

    Args:
        max_delay: the integer argument

    Return:
        return an async task
    '''

    task = asyncio.create_task(wait_random(max_delay))

    return task
