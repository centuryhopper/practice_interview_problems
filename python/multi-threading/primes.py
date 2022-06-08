from threading import Thread
from multiprocessing import Process, Pool, Value, Array
import multiprocessing as mp
import concurrent.futures
from typing import Final
import numpy as np
import time
import math


# UPPER_BOUND: Final = int(1e8)
NUM_THREADS: Final = 8
# cnt = 0
# lock = None
# primes = np.ones(UPPER_BOUND+1, dtype=np.bool)

class Siever:

    def __init__(self):
        # self.cnt = 0
        pass

    # def init(self, l):
    #     global lock
    #     lock = l

    def sieveSingleThread(self, primes: np.ndarray, startInd: int, UPPER_BOUND: int) -> None:
        while startInd * startInd <= UPPER_BOUND:
            if primes[startInd]:
                primes[startInd*startInd :: startInd] = False
            startInd += 2

    # 8 threads will count all the primes in its segment
    # for 1e8, the first thread will count from 0 to 12.5 million, exclusive;
    # the second thread will count from 12.5 million to 25 million, exclusive;
    # and so on and so forth
    def count_and_add_primes(self, args):
        start, primes, cnt = args[0], args[1], args[2]
        offset = 12500000
        for i in range(start+1, start+offset, 2):
                cnt.value += 1
                print(cnt.value)





if __name__ == '__main__':

    # starting points for the sieve, one for each thread
    # primeNums = np.array([3, 5, 7, 11, 13, 17, 31, 41])

    # primeNums = np.array([3, 5, 7, 11, 13, 17, 31])

    UPPER_BOUND = int(1e8)
    primes = np.ones(UPPER_BOUND+1, dtype=np.bool)
    # 0 and 1 are not prime numbers
    primes[0], primes[1] = False, False
    # atomic integer
    # primeCounter = Value('i', 1)
    atomicCnt = Value('i', 0)

    s = Siever()
    l = mp.Lock()
    start = time.time()

    # for num in primeNums:
    s.sieveSingleThread(primes, 3, UPPER_BOUND)

    # results = [2]
    # total = 2
    # for i in range(3, UPPER_BOUND, 2):
    #     if primes[i]:
    #         results.append(i)
    #         total += i


    lstOfArgs = [
        (0, primes, atomicCnt),
        (12500000, primes, atomicCnt),
        (25000000, primes, atomicCnt),
        (37500000, primes, atomicCnt),
        (50000000, primes, atomicCnt),
        (62500000, primes, atomicCnt),
        (75000000, primes, atomicCnt),
        (87500000, primes, atomicCnt),
        ]

    # shared_array = mp.Array('i', primes)


    pool = Pool(processes=8)
    result = pool.map(s.count_and_add_primes, lstOfArgs)
    pool.close()
    pool.join()

    print('{} ms'.format((time.time() - start) * 1e3))

    # print('total number of primes under 10^8: {}'.format(len(results)))
    print('total sum of all primes under 10^8: {}'.format(s.cnt))

    # print('largest 10 primes: {}'.format(results[-10::]))

    print('done')










    pass


