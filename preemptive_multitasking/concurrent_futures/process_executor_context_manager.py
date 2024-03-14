"""
This script demonstrates how to use the ProcessPoolExecutor from the concurrent.futures module to run multiple tasks
"""

from concurrent import futures
from time import sleep, time


def wait_a_moment(t: float) -> str:
    """
    Function to simulate a long running task

    :param t:
    :return:
    """
    print(f"Sleeping for {t} seconds")
    sleep(t)
    end = time()
    print(f"Done sleeping for {t} seconds. Time is {end:0.0f}")
    return f"Awaked after {t} seconds of sleep. Time is {end:0.0f}"


if __name__ == "__main__":
    # max_workers is the number of processes that can run concurrently
    # If max_workers is None or not given, it will default to the number of processors on the machine
    with futures.ProcessPoolExecutor(max_workers=3) as executor:
        print(f"Start time is {time():0.0f}")

        f1 = executor.submit(wait_a_moment, 10)
        f2 = executor.submit(wait_a_moment, 2)
        f3 = executor.submit(wait_a_moment, 6)
        f4 = executor.submit(wait_a_moment, 5)
        f5 = executor.submit(wait_a_moment, 3)

        print("\nAll tasks submitted")

    print("All tasks completed")

    # The result method will block until the task is completed
    # If the task is not completed, it will raise a concurrent.futures.TimeoutError
    print("\nResults:")
    for f in [f1, f2, f3, f4, f5]:
        print(f.result())