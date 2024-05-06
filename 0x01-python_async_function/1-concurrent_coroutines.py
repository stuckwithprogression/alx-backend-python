#!/usr/bin/env python3
'''asyncronous coroutine
'''

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''takes in 2 integer arguments and spawn a particular variable a number of
    times with the specified maximum delay

    Args:
        n: the number of times to spawn wait_random variable
        max_delay: the specified maximum delay

    Return:
        return a list of all the delays in async order as float
    '''

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
