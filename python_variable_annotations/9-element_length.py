#!/usr/bin/env python3
"""
Module for task 9.
Provides a type-annotated function that calculates the length of each
element in an iterable sequence.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples containing
    each element and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
