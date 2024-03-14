import threading


class RaceConditionThread(threading.Thread):
    """Class to demonstrate a race condition
    """

    # Class variable to lock the critical section
    # Be sure to use lock with critical sections to not reach deadlocks!
    # "Deadlocks" are a common problem in concurrent programming, where two or more threads are blocked forever.
    lock = threading.Lock()

    # Class variable to store the shared resource
    shared_resource = 0

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(1_000_000):
            with RaceConditionThread.lock:
                RaceConditionThread.shared_resource += 1
        print(f"{self.name} finished")


def main():
    threads = []
    for i in range(5):
        thread = RaceConditionThread(f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\nShared resource is {RaceConditionThread.shared_resource}")


main()