#!/usr/bin/env python3
'''annotation with appropriate types
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''iterable function

    Args:
        lst: an iterable list

    Return:
        return a list of tuples with their respective length
    '''

    return [(i, len(i)) for i in lst]
