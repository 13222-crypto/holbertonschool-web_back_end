#!/usr/bin/env python3
"""
Module for task 5.
Provides a type-annotated function that calculates the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as input and returns their sum as a float.
    """
    return float(sum(input_list))
