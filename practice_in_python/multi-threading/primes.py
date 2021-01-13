from threading import Thread
from typing import Final
import numpy as np
import time
import math

UPPER_BOUND: Final = 10**8
NUM_THREADS: Final = 8

def SieveEmForGood(startInd: int, endInd: int, primes: list[bool]) -> None:

    res = int(math.sqrt(endInd))
    for i in range(startInd, res, 2):
        if primes[i]:
            for j in range(i*i, endInd, i):
                primes[j] = False


if __name__ == '__main__':

    # starting points for the sieve, one for each thread
    primeNums = np.array([3, 5, 7, 11, 13, 17, 31, 41])

    # Set the initial values of the primes array
    primes = np.array([True] * (UPPER_BOUND + 1))
    primes[0], primes[1] = False, False

    threads = np.array([])

    start = time.time()

    for i in range(NUM_THREADS):
        threads = np.append(threads, Thread(target=SieveEmForGood, args=(primeNums[i], UPPER_BOUND, primes)),)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()

    print('{} ms'.format((end - start) * 1e3))

    results = [2]
    total = 2

    fast_append = results.append

    for i in range(3, UPPER_BOUND, 2):

        if primes[i]:
            fast_append(i)
            total += i

    print('total number of primes under 10^8: {}'.format(len(results)))
    print('total sum of all primes under 10^8: {}'.format(total))

    print('largest 10 primes: {}'.format(results[-10:]))

    print('done')










    pass


