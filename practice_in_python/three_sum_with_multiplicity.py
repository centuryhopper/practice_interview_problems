from collections import defaultdict

class Solution:
    def threeSumMulti(self, lst: List[int], target: int) -> int:
        mod = 7 + (10**9)
        n = len(lst)
        res = 0
        for i in range(n):
            # new defaultdict for every i
            cnter = defaultdict(int)
            for j in range(i+1, n):
                kVal = target - (lst[i] + lst[j])

                # this if check isnt needed for default dictionaries but
                # is just here for clarity
                if cnter[kVal] > 0:
                    res += cnter[kVal]
                    res %= mod
                # visit this value current value for every i
                cnter[lst[j]] += 1
        return res

    

























    # brute force
    # def threeSumMulti(self, lst: List[int], target: int) -> int:
        # d = defaultdict(int)
        # n = len(lst)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             res = lst[i] + lst[j] + lst[k]
        #             if res == target:
        #                 d[(lst[i], lst[j], lst[k])] += 1
        # return sum (d.values()) % (7 + 10**9)