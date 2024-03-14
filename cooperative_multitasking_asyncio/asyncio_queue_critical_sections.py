import threading
import queue
import time

# Creating a global queue instance
shared_queue = queue.Queue()
# A lock to synchronize access to critical sections
lock = threading.Lock()


def producer(q, n):
    for i in range(n):
        time.sleep(0.5)  # Simulate a time-consuming operation
        item = f"Item {i}"
        with lock:  # Entering the critical section
            q.put(item)
            print(f"{threading.current_thread().name} has added {item} to the queue.")
    # Signal the end of production
    q.put(None)


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            # End signal received
            q.put(None)  # Important to allow other consumers to notice the end as well
            break
        with lock:  # Entering the critical section
            print(f"{threading.current_thread().name} has taken {item} from the queue and processed it.")
        time.sleep(1)  # Simulate processing time


def main():
    producers = 2
    consumers = 2

    # Create and start producer threads
    for i in range(producers):
        threading.Thread(target=producer, args=(shared_queue, 5), name=f"Producer-{i}").start()

    # Create and start consumer threads
    for i in range(consumers):
        threading.Thread(target=consumer, args=(shared_queue,), name=f"Consumer-{i}").start()


if __name__ == "__main__":
    main()
