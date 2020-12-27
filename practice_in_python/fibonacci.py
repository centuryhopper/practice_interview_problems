import time as t



class Fibonacci:

    # def __init__(self, n: int):
    #     self.n = n

    def fib_recursive(self, n : int) -> int:
        if n < 0: raise Exception('sorry, only non-negative inputs are permitted')

        if n < 2: return n
        return self.fib_recursive(n - 2) + self.fib_recursive(n - 1)

    def fib_memo(self, n: int, m: dict[int, int]) -> int:

        if n < 0: raise Exception('sorry, only non-negative inputs are permitted')

        # base case
        if n < 2: return n

        # If we've already cached this result, just go ahead and return it.
        if n in m: return m[n]

        # Compute the result using the recurrence relation as before, but cache the
        # result for later reuse.
        res = self.fib_memo(n - 1, m) + self.fib_memo(n - 2, m)
        m[n] = res
        return res

    def fib_dp(self, n: int) -> int:

        if n < 0: raise Exception('sorry, only non-negative inputs are permitted')

        a = [0, 1]
        for i in range(2, n + 1):
            a[i % 2] = a[0] + a[1]

        return a[n % 2]


f = Fibonacci()
# rec_ans = f.fib_recursive(10)
# print(rec_ans)

start = t.time_ns()
# memo_ans = f.fib_memo(100, {})
# print(memo_ans)
memoLst = [f.fib_memo(i, {}) for i in range(100)]
print(memoLst)
print('total time for memo: ', t.time_ns() - start)

print('--------------------------------------------')

start = t.time_ns()
# dp_ans = f.fib_dp(100)
# print(dp_ans)
dpLst = [f.fib_dp(i) for i in range(100)]
print(dpLst)
print('total time for dp: ', t.time_ns() - start)

