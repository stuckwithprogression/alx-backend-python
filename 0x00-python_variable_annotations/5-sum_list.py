#!/usr/bin/env python3
'''sum of lists of floats
'''

from typing import List


def sum_list(input_list: List[float] = []) -> float:
    '''get the sum of lists of floats passed as argument

    Args:
        input_list: the list of floats

    Return:
        return the sum of the list of the floats
    '''

    return sum(input_list)
