import sys
import time
import multiprocessing as mp
import numpy as np
import os

# Bissey's code from the class I TAed for, so credit goes to him


def get_primes_warmup(n):
    """
    Serial SieveOfEratosthenes to n.
    n will be sqrt of segment_top of thread calling this.
            1. init np Array
            2. mark multiples of smallest unmarked odd numbers up to the sqrt(n)
            3. nonzero indices are the primes
            4. adjust output keeping in mind we only tracked odd nums
    params:
                    n: find primes from 1 to this number
    """
    # sieve only accounts for odds
    sieve = np.full(n // 2, True)
    # first odd (1) is not prime, must be marked outside of loop
    sieve[0] = False

    sqrtN = int(n ** .5)

    for candidate in range(3, sqrtN + 1, 2):
        if sieve[candidate // 2]:
            # set every i'th starting at square of i to not PRIME
            # replace double for loop with numpy operation
            sieve[candidate ** 2 // 2:: candidate] = False

    indices = np.flatnonzero(sieve)

    # scale up from odds only
    final_primes = 1 + 2*indices
    return final_primes


def get_primes_from_segment(labelled_segment):
    """
    Find all primes in the given segment. (uses numpy)

    This will be called by each of our 8 threads,

    params:
            labelled_segment: tuple(thread_num, tuple(segment_bottom, segment_top))
    returns:
            thread_num: index of thread calling this.
            primes_from_segment: numpy ndarray of primes
    """
    # make sure we are starting and stopping at odds
    thread_num, range = labelled_segment
    segment_bottom, segment_top = range

    # make top and bottom odd if they aren't already
    if segment_bottom % 2 == 0:
        segment_bottom += 1
    if segment_top % 2 == 0:
        segment_top -= 1

    # create sieve for this segment
    segment_size = segment_top - segment_bottom
    # sieve length is half of segment size....no evens
    sieve_length = (segment_size + 2) // 2
    sieve = np.full(sieve_length, True)

    # get primes up to sqrt of segment_top
    warmup_primes = get_primes_warmup(int(segment_top ** .5) + 1)

    # mark multiples of each prime in warmups
    for prime_i in warmup_primes:
        diff = segment_bottom % prime_i
        prime_i_multiple = segment_bottom - diff
        # add prime_i until we reach odd above segment bottom
        if prime_i_multiple % 2 == 1 and prime_i_multiple >= segment_bottom:
            pass
        else:
            prime_i_multiple += prime_i
            if prime_i_multiple % 2 == 0:
                prime_i_multiple += prime_i

        # get the sieve start index which will represent the first odd multiple in segment
        sieve_index = (prime_i_multiple - segment_bottom) // 2
        # mark each index false for every multiple of prime_i
        sieve[sieve_index: sieve_length: prime_i] = False

        # mark current prime_i as true if in current segment
        if segment_top >= prime_i >= segment_bottom:
            sieve[(prime_i - segment_bottom) // 2] = True

    indexed_primes = np.flatnonzero(sieve)

    # scale back from just odds
    primes_from_segment = segment_bottom + (2 * indexed_primes)
    return thread_num, primes_from_segment


def get_primes_multithread_segment(bigN, n_threads):
    """
    Function used to manage threads and accumulate data when they complete.

    params:
            bigN: find primes under this number
            n_threads: utilize this many threads in the pool

    returns:
            last10: ndarray of largest 10 primes
            num_primes_total: int (total counted primes)
            prime_sum: int (sum of primes in all threads)
    """
    # split range of numbers into n into n/thread segments
    segment_size = bigN // n_threads
    segments = [[i, i + segment_size] for i in range(2, bigN, segment_size)]
    # cap segment at n
    segments[len(segments) - 1][1] = bigN

    # create pool with given number of threads
    proc_pool = mp.Pool(n_threads)
    labeled_segs = []
    for idx, segment in enumerate(segments):
        labeled_segs.append((idx, segment))

    # map each thread's output to a list of lists of prime segments
    prime_segments = proc_pool.map(get_primes_from_segment, labeled_segs)
    print(len(prime_segments))

    num_primes_total = 0
    prime_sum = 0

    last10 = None
    # count and sum our findings running through each segment
    for thread_num, seg in prime_segments:
        num_primes_total += len(seg)
        prime_sum = sum(seg) + prime_sum

        if thread_num == n_threads - 1:
            last10 = seg[-10::]

    # must add 2 back in here!
    return last10, num_primes_total + 1, prime_sum + 2


if __name__ == '__main__':
    """
    Keep Time and Print everything in Main.
    """
    # print(os.getcwd())

    bigN = 10 ** 8
    n_threads = 8

    start = time.time()
    last10, num_primes, sum_primes = \
        get_primes_multithread_segment(bigN, n_threads)
    end = time.time()

    exec_time = round((end - start), 4)
    with open('./multi-threading/primes_final.txt', 'w') as f:
        sys.stdout = f
        print('current output!')
        print(f'<{exec_time} seconds> <{num_primes}> <{sum_primes}>')
        print(f'<{last10}>')
