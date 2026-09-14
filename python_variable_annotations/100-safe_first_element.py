#!/usr/bin/env python3
"""
Module for task 10.
Provides a duck-typed function that safely returns the first element
of a sequence or None if empty.
"""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
