#!/usr/bin/env python3
"""
Module for task 0.
Provides an asynchronous generator yielding random numbers.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, asynchronously waits 1 second each iteration,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
