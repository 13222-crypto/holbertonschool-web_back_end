#!/usr/bin/env python3
"""
Module for task 7.
Provides a type-annotated function that returns a tuple containing
a string and the square of an int or float as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v, and returns a tuple with k
    and the square of v as a float.
    """
    return (k, float(v ** 2))
