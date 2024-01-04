#!/usr/bin/env python3
"""task1. Let's execute multiple coroutines
at the same time with async"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called wait_n that takes in 2 int arguments
    and returns the list of all the delays (float values)"""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
