#!/usr/bin/env python3
"""
Module for task 4.
Spawns task_wait_random n times concurrently and returns sorted delays.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns the list of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
