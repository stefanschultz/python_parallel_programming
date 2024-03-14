"""
Typical topics of cooperative multitasking with asyncio are:
- asyncio event loop: run_forever, run_until_complete, stop
- asyncio tasks: create_task, gather, wait, as_completed
- asyncio coroutines: async, await
- asyncio futures: Future, ensure_future, set_result, set_exception
- asyncio streams: open_connection, start_server
- asyncio protocols: Protocol, StreamReader, StreamWriter
- asyncio transports: Transport, BaseTransport
- asyncio queues: Queue, PriorityQueue, LifoQueue
- asyncio locks: Lock, RLock
- asyncio semaphores: Semaphore
- asyncio conditions: Condition
- asyncio barriers: Barrier
- asyncio subprocesses: create_subprocess_exec, create_subprocess_shell
- asynchronous comprehensions: async for, async with
- asynchronous context managers: async with
- asynchronous generators: async yield
- ... and many more

Event loop:
An event loop is a loop that waits for events to occur and then reacts to them. In the context of asyncio,
an event loop is a loop that waits for coroutines to produce results and then reacts to them. The event loop is the
core of asyncio. It is the central execution device provided by the asyncio module. The event loop

Coroutines:
Coroutines are functions that can pause and resume their execution. They are used to write asynchronous code in Python.

Async and await:
The async and await keywords are used to define coroutines. The async keyword is used to define a coroutine.
The await keyword is used to pause the execution of a coroutine until the result of another coroutine is available.

Awaitable objects:
An awaitable object is an object that can be used in an await expression. The following types of objects are awaitable:
- Coroutines
- Tasks
- Futures
- Streams
- Synchronization primitives (locks, semaphores, etc.)
- Queues
- Subprocesses
- ... and many more
"""

import asyncio

# The asyncio.sleep function is a coroutine that pauses the execution of the current coroutine for a given number of seconds
async def sleep_and_print(n: int) -> int:
    print(f"Sleeping for {n} seconds")
    await asyncio.sleep(n)
    print(f"Done sleeping for {n} seconds")
    return n


async def main_synchronous():
    # This is a coroutine that calls another coroutine to show that all tasks are running not concurrently (parallel).
    # The coroutines are running in a sequential manner.
    await sleep_and_print(3)
    await sleep_and_print(2)
    await sleep_and_print(1)
# asyncio.run(main1())


async def main_multitasking():
    # The asyncio.create_task function is used to create a task from a coroutine
    # The task is automatically scheduled for execution in the event loop
    t1 = asyncio.create_task(sleep_and_print(3))
    t2 = asyncio.create_task(sleep_and_print(2))
    t3 = asyncio.create_task(sleep_and_print(1))

    tasks = (t1, t2, t3)

    # The awaitable asyncio.gather function is used to wait for the results of multiple coroutines
    # It returns a list of the results
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

    # Here we are using the results. If you are not interested in the results, is it meaning "Fire and Forget".
    # Fire and Forget is a design pattern where the caller does not wait for the result of an operation.
asyncio.run(main_multitasking())
