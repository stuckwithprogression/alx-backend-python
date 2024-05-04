#!/usr/bin/env python3
'''tuple of a string and an integer/float
'''

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''makes a tuple out of a string and an integer/float

    Args:
        k: the string
        v: the integer/float

    Return:
        return a tuple
    '''

    return k, v**2
