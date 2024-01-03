#!/usr/bin/env python3
"""task8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
    """

    def fnc(n: float):
        return (n * multiplier)

    return (fnc)
