#!/usr/bin/env python3
import random
import asyncio

"""The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10. """


async def async_generator():
    """Loop coroutine 10 times """
    for _ in range(10):
        await asyncio.sleep(1)
        # pausing func using yield instead of returning
        yield random.uniform(0, 10)
