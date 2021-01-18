import numpy as np


class Solution:

    # brute force recursive (time limit exceeded)

    # start at -1 and add the element we will recurse on
    def helper(self, lst: list[int], i: int) -> int:
        if i >= len(lst) - 2:
            return 0

        return min(lst[i+1] + self.helper(lst, i+1), lst[i+2] + self.helper(lst, i+2))

    def helper_memo(self, lst: list[int], i: int, memo: dict[int, int]) -> int:
        if i >= len(lst) - 2:
            memo[i] = 0
            return 0
        if i in memo:
            return memo[i]

        memo[i] = min(lst[i+1] + self.helper_memo(lst, i+1, {}),
                      lst[i+2] + self.helper_memo(lst, i+2, {}))

        return memo[i]

    def helper_dp(self, lst: np.ndarray) -> int:
        # assumes array size is at least 2

        for i in range(2, lst.size):
            lst[i] += min(lst[i-1], lst[i-2])

        last, secondToLast = lst.size - 1, lst.size - 2

        return min(lst[last], lst[secondToLast])

    def minCostClimbingStairs(self, lst: List[int]) -> int:
        return self.helper_dp(np.array(lst, dtype=int))
