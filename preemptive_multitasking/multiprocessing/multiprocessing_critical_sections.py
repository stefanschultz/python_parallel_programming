from random import random
import multiprocessing
from time import sleep


class PrimNumberProcess(multiprocessing.Process):
    """Thread class to check if a number is a prime number
    """
    def __init__(self, number, lock):
        super().__init__()
        self.number = number
        self.lock = lock

    def run(self):
        i = 2
        while i < self.number:
            if self.number % i == 0:
                self.lock.acquire()
                print(f"{self.number} is not a prime number")
                self.lock.release()
                return
            i += 1
        self.lock.acquire()
        print(f"{self.number} is a prime number")
        self.lock.release()


def main():
    processes = []
    prompt = "Enter a number or type \"exit\": "
    number = 1
    lock = multiprocessing.Lock()

    your_input = input(prompt)

    while your_input != "exit":
        try:
            number = int(your_input)
            process = PrimNumberProcess(number, lock)
            processes.append(process)
            process.start()
        except ValueError as e:
            with lock:
                print(f"Error: unable to start process for {number}. {e}")
        with lock:
            your_input = input(prompt)

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()