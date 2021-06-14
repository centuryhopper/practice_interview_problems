from heapq import heappush, heappop, heapify


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # brute force algorithm
        def rec(nums, n, k, i) -> int:
            # bounds check
            if i >= n:
                return 0
            if i == n - 1:
                return nums[i]
            maxVal = float('-inf')
            # always have up to k choices at any given point
            for x in range(1, k+1):
                # move forward x steps
                maxVal = max(maxVal, nums[i] + rec(nums, n, k, i+x))
            return maxVal

        # brute force dp
        # n = len(nums)
        # dp = [0] * n
        # dp[n-1] = nums[n-1]
        # for i in range(n-2, -1,-1):
        #     getMax = float('-inf')
        #     for j in range(i+1,min(i+1+k, n)):
        #         getMax = max(getMax, dp[j])
        #     dp[i] = nums[i] + getMax
        # print(dp)
        # return dp[0]


        # my final solution using heap Time: O(n log n) Space: O(n) for the dp array
        n = len(nums)
        dp = [0] * n
        dp[n-1] = nums[n-1]
        h = []
        heapify(h)
        h.append((-nums[n-1], n-1))
        for i in range(n-2, -1, -1):
            # if it's reachable, we'll take it and add to nums[i],
            # otherwise keep trying
            while h[0][1] > i + k:
                heappop(h)
            dp[i] = nums[i] + -h[0][0]
            heappush(h, (-dp[i], i))

        # print(dp)
        return dp[0]
