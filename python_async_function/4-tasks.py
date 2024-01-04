#!/usr/bin/env python3
"""4. Tasks"""


import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """defines an asynchronous function task_wait_n that uses asyncio.gather
    to concurrently execute the task_wait_random function n times"""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
