from random import random
import threading
from time import sleep


class PrimNumberThread(threading.Thread):
    """Thread class to check if a number is a prime number
    """

    # Class variable to lock the critical section
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        i = 2
        while i < self.number:
            if self.number % i == 0:
                PrimNumberThread.lock.acquire()
                print(f"{self.number} is not a prime number")
                PrimNumberThread.lock.release()
                return
            i += 1
        PrimNumberThread.lock.acquire()
        print(f"{self.number} is a prime number")
        PrimNumberThread.lock.release()


def main():
    threads = []
    prompt = "Enter a number or type \"exit\": "
    number = 1

    your_input = input(prompt)

    while your_input != "exit":
        try:
            number = int(your_input)
            thread = PrimNumberThread(number)
            threads.append(thread)
            thread.start()
        except ValueError as e:
            with PrimNumberThread.lock:
                print(f"Error: unable to start thread for {number}. {e}")
        with PrimNumberThread.lock:
            your_input = input(prompt)

    for thread in threads:
        thread.join()


main()