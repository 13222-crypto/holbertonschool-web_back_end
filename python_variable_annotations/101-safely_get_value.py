#!/usr/bin/env python3
"""
Module for task 11.
Provides a type-annotated function using TypeVar to safely retrieve
values from a mapping dictionary.
"""
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Retrieves a value from a mapping by key, returning default if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
