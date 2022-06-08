from collections import deque

class Solution:
    # radix sorting method
    def radixSort(self, nums: list[int]) -> None:
        prevMult, mult = 1, 10
        maxVal = max(nums)
        # print(maxVal)
        buckets = [deque() for _ in range(10)]
        while maxVal > 0:
            for num in nums:
                bucketInd = (num % mult) // prevMult
                buckets[bucketInd].append(num)
            prevMult = mult
            mult *= 10
            maxVal //= 10
            i = 0
            # repopulate nums using values from lst of deques
            for bucket in buckets:
                while bucket:
                    nums[i] = bucket.popleft()
                    i+=1
            # debug
            # print(nums, maxVal)



    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2: return 0

        self.radixSort(nums)

        maxDiff = 0
        for i in range(1, len(nums)):
            maxDiff = max(maxDiff, nums[i] - nums[i-1])
        return maxDiff





