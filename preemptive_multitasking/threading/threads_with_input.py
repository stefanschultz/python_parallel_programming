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
            print(f"Error: unable to start thread for {number}. {e}")
        your_input = input(prompt)

    for thread in threads:
        thread.join()


main()