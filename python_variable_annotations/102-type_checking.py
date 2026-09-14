#!/usr/bin/env python3
"""
Module for task 12.
Provides a type-checked function to repeat elements in a tuple/list.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into an array by repeating each element factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
