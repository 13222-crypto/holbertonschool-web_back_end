#!/usr/bin/env python3
"""
Module for task 8.
Provides a type-annotated function that creates a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    """
    def multiply(n: float) -> float:
        """Multiplies a given float by the multiplier."""
        return n * multiplier

    return multiply
