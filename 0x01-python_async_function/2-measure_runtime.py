#!/usr/bin/env python3
'''measure runtime
'''

import asyncio
import random
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    '''measures the total execution time for an asynchronous function

    Args:
        n: first integer argument
        max_delay: second integer argument (default to 10)

    Return:
        return a float
    '''

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time

    return (elapsed_time / n)
