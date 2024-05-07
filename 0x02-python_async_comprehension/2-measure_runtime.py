#!/usr/bin/env python3
'''measure runtime coroutine
'''

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''coroutine that executes and async comprehension four times in parallel
    and measures the total runtime

    Return:
        return the total runtime
    '''

    start_time = time.perf_counter()
    task = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time
