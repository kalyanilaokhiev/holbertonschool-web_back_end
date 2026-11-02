#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an int
argument that waits for a random delay between 0 and max_delay
seconds and eventually returns it."""

import random
import asyncio


async def wait_random(max_delay=10.0):
    """wits for random delay and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
