#!/usr/bin/python3
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    print(numbers)
    start_time = time.time()
    
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

