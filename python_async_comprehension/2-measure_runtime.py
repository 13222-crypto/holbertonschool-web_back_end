#!/usr/bin/env python3
"""
Module for task 2.
Measures total runtime for executing four parallel async comprehensions.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.
    """
    start_time: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.time()
    return end_time - start_time
