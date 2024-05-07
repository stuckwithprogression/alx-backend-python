#!/usr/bin/env python3
'''async generator coroutine
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''coroutine that loops ten times, asynchronously wait for one second each
    time, then yields a random number between 0 and 10

    Return:
        return a random number between 0 and 10
    '''

    for _ in range(10):
        await asyncio.sleep(1)

        yield random.uniform(0, 10)
