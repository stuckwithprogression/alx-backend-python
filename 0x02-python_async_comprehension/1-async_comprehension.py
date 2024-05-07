#!/usr/bin/env python3
'''async comprehension coroutine
'''

import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''coroutine that collects 10 random numbers using an async comprehension
    over an async generator

    Return:
        return the 10 random numbers
    '''

    random_numbers = [i async for i in async_generator()]

    return random_numbers
