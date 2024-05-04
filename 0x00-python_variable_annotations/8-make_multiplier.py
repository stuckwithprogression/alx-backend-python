#!/usr/bin/env python3
'''multiplication function
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplies a float multiplier by another float

    Args:
        multiplier: the float multiplier

    Return:
        return a function that multiplies a float by a multiplier
    '''

    def func_multiplier(num: float) -> float:
        '''multiplies a float by a multiplier

        Args:
            num: the float to multiply by a multiplier

        Return:
            return the multiplication of num and the multiplier
        '''

        return multiplier * num

    return func_multiplier
