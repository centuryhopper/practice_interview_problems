from multiprocessing import Pool
import time
from sympy import isprime
# from sympy.ntheory import primerange




if __name__ == '__main__':

    t = time.time()
    p = Pool()
    result = p.map(isprime, range(int(1e8)))
    p.close()
    p.join()

    print('pool took: {} seconds'.format(time.time() - t))



