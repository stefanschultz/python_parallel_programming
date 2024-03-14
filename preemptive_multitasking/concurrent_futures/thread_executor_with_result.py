from concurrent import futures
from time import time


def approximate_pi(n):
    """Approximate PI using the John Wallis formula

    :param n:
    """
    pi = 2
    for i in range(1, n):
        pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi


def run_tasks_and_wait_until_all_completed():
    """Run and wait until all tasks are completed.

    :return:
    """
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        start_time = time()
        print("Start tasks...")
        f1 = executor.submit(approximate_pi, 10000000)
        f2 = executor.submit(approximate_pi, 5000000)
        print(f"PI is approximately {f1.result():0.10f}")
        print(f"PI is approximately {f2.result():0.10f}")
        print(f"All tasks completed after {time() - start_time:0.0f} seconds.")


def run_tasks_wait_as_completed():
    """Run tasks and wait as they are completed.

    :return:
    """
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        N = (10000000, 5000000, 200000, 100, 50000)
        with futures.ThreadPoolExecutor(max_workers=4) as executor:
            start_time = time()
            print("Start tasks...")
            fs = {executor.submit(approximate_pi, n): n for n in N}
            for f in futures.as_completed(fs):
                n = fs[f]
                print(f"PI is approximately {f.result():0.10f} for n = {n}")
        print(f"All tasks completed after {time() - start_time:0.0f} seconds.")

def run_tasks_wait_with_event():
    """Run tasks and wait with defined event.

    :return:
    """
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        N = (10000000, 5000000, 200000, 100, 50000)
        with futures.ThreadPoolExecutor(max_workers=4) as executor:
            start_time = time()
            print("Start tasks...")
            fs = {executor.submit(approximate_pi, n): n for n in N}
            res = futures.wait(fs)
            for f in res.done:
                n = fs[f]
                print(f"PI is approximately {f.result():0.10f} for n = {n}")
        print(f"All tasks completed after {time() - start_time:0.0f} seconds.")


def run_tasks_map():
    """Run tasks using map.

    :return:
    """
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        N = (10000000, 5000000, 200000, 100, 50000)
        start_time = time()
        print("Start tasks...")
        results = executor.map(approximate_pi, N, chunksize=2)
        for n, pi in zip(N, results):
            print(f"PI is approximately {pi:0.10f} for n = {n}")
        print(f"All tasks completed after {time() - start_time:0.0f} seconds.")


if __name__ == "__main__":
    # run_tasks_and_wait_until_all_completed()
    # run_tasks_wait_as_completed()
    # run_tasks_wait_with_event()
    run_tasks_map()