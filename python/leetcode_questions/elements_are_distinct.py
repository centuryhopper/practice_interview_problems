import types
from numpy import random
from time import time, time_ns

# O(n^2) time, O(1) space approach
# nums should be a generator method
def elements_are_distinct_brute_force(elems: list[any]) -> bool:
    for i in range(len(elems) - 1):
        for j in range(i+1, len(elems)):
            if elems[j] == elems[i]:
                return False
    return True

# O(n) time and space approach
# nums should be a generator method
def elements_are_distinct(nums: types.GeneratorType) -> bool:
    st = set()
    for num in nums:
        if num in st: return False
        st.add(num)
    return True

def number_generator(start:int, end:int):
    for i in range(start, end):
        yield i
        print(i)

if __name__ == '__main__':

    start = time()
    print(elements_are_distinct_brute_force([i for i in range(10000)]))
    stop = time()
    print('brute force approach time: {} seconds'.format(stop - start))

    start = time()
    print(elements_are_distinct((i for i in range(10000000))))
    stop = time()

    print('optimized approach time: {} seconds'.format(stop - start))

