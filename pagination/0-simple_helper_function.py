#!/usr/bin/env python3
"""
Module providing a helper function for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)
