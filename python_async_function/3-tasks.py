#!/usr/bin/env python3
"""
Module for task 3.
Provides a function that returns an asyncio.Task for wait_random.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes max_delay and returns an asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
