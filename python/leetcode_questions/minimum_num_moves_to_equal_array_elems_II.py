

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # n log n runtime because of sorting
        nums.sort()
        cnt = 0
        median = nums[len(nums)//2]
        # check the distance between each element and the median
        # and sum them up
        for num in nums:
            cnt += abs(median - num)
        return cnt



