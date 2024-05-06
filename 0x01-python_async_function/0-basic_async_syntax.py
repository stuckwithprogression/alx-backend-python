#!/usr/bin/env python3
'''asynchronous coroutine
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''takes in an integer argument with a default value of 10, that waits for
    a random delay between 0 and maximum delay seconds

    Args:
        max_delay: the integer argument with a default value of 10

    Return:
        return a floating point value of the maximum delay
    '''

    delay: float = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
