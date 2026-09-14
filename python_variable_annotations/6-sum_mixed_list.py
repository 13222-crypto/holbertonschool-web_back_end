#!/usr/bin/env python3
"""
Module for task 6.
Provides a type-annotated function that calculates the sum of a list
containing integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum as a float.
    """
    return float(sum(mxd_lst))
