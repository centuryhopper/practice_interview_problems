import numpy as np
'''
Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
'''


class Solution:

    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n

        lst = np.array([0] * (n + 1), dtype=int)
        lst[1] = 1

        # print(lst)

        retVal = 1

        for i in range(n):
            if 2*i > n or 2*i + 1 > n:
                break

            if 2 <= 2*i and 2*i <= n:
                lst[2*i] = lst[i]
            if 2 <= 2*i + 1 and 2*i + 1 <= n:
                lst[2*i + 1] = lst[i] + lst[i + 1]

            compute = max(lst[2*i], lst[2*i + 1])
            retVal = max(compute, retVal)

        # print(lst)

        return retVal

# Solution.getMaximumGenerated(16)