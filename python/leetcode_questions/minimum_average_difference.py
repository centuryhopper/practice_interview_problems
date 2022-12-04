import math


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        suffixSum = [0] * n
        prefixSum[0] = nums[0]
        suffixSum[-1] = nums[-1]
        for i in range(1,n):
            prefixSum[i] = nums[i]+prefixSum[i-1]
        for i in range(n-2,-1,-1):
            suffixSum[i] = nums[i]+suffixSum[i+1]
        # print(prefixSum)
        # print(suffixSum)

        absDiffs = [0] * n
        # formula only works for up to n-1
        for i in range(n-1):
            part1 = prefixSum[i] // (i+1)
            part2 = suffixSum[n-(n-1-i)] // (n-1-i)
            absDiffs[i] = abs(part1 - part2)

        absDiffs[-1] = prefixSum[-1] // n
        # print(absDiffs)

        minIndex = n-1
        minVal = math.inf
        for i,val in enumerate(absDiffs):
            if val < minVal:
                minVal = val
                minIndex = i
        return minIndex


