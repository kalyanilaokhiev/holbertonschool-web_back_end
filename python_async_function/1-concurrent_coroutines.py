#!/usr/bin/env python3
"""Import wait_random from the previous python file
that you've written and write an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay"""

import asyncio
from typing import List

# Import wait_random from the previous python file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs n amount of runs with a max of max_delay concurrenly
    and orders it in ascending order """
    n_runs = []
    delays = []

    # creating a list of n coroutine tasks to run at the same time
    for i in range(n):
        n_runs.append(wait_random(max_delay))

    # orders the time it takes in ascending order as each task completes
    for run in asyncio.as_completed(n_runs):
        delay = await run
        delays.append(delay)

    return (delays)
