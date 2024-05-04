#!/usr/bin/env python3
'''sum of list of intergers and floats
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''gets the sum of list of integers and floats

    Args:
        mxd_list: list of integers and floats

    Return:
        return the sum of the mixed list of integers and floats as int
    '''

    return sum(mxd_lst)
