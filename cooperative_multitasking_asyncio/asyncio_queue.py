import asyncio

# The asyncio.Queue class is a queue that can be used to communicate between coroutines
# It is a first-in, first-out (FIFO) data structure


async def producer(queue: asyncio.Queue, n: int):
    """A coroutine that puts numbers into the queue."""
    for i in range(n):
        # Simulate some computation or delay
        await asyncio.sleep(1)
        print(f'Producer {n}: adding {i} to the queue')
        await queue.put(i)


async def consumer(queue: asyncio.Queue, n: int):
    """A coroutine that removes and processes numbers from the queue."""
    while True:
        # Wait for an item from the queue
        item = await queue.get()
        print(f'Consumer {n}: got {item} from the queue and processed it')
        # Mark the task as done
        queue.task_done()


async def main_queue():
    # Create a queue
    q = asyncio.Queue()

    # Start producers and consumers
    producers = [asyncio.create_task(producer(q, i)) for i in range(6)]  # 3 producers
    consumers = [asyncio.create_task(consumer(q, i)) for i in range(2)]  # 2 consumers

    # Wait until all producers are finished
    await asyncio.gather(*producers)
    # Wait until all items in the queue have been processed
    await q.join()
    # Cancel consumers (in a real application, you might handle this more gracefully)
    for c in consumers:
        c.cancel()


# Run the main_queue coroutine
asyncio.run(main_queue())
