from random import random
import threading
from time import sleep


class PrimNumberThread(threading.Thread):
    """Thread class to check if a number is a prime number
    """
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        i = 2
        while i < self.number:
            if self.number % i == 0:
                print(f"{self.number} is not a prime number")
                return
            i += 1
        print(f"{self.number} is a prime number")


def main():
    numbers = [15485863, 15485867, 15485869, 15485917, 15485927, 15485933, 15485941, 15485953, 15485957, 15485963]
    threads = []

    print(f"Start tasks...")

    for number in numbers:
        try:
            thread = PrimNumberThread(number)
            threads.append(thread)
            thread.start()
            sleep(random() * 2)
        except Exception as e:
            print(f"Error: unable to start thread for {number}. {e}")

    for thread in threads:
        thread.join()

    print("All tasks completed")


main()