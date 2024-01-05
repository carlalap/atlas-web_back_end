#!/usr/bin/env python3
"""task2. Run time for four parallel comprehensions"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather."""
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
