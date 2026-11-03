#!/usr/bin/env python3
"""Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehnesion 4 times in parallel"""
    start_time = time.perf_counter()

    # run 4 tasks at the same time
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    # elapsed time
    total_time = end_time - start_time

    return total_time
