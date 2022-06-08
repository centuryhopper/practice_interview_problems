import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums,target)
        if i == len(nums): return -1
        if nums[i] != target: return -1
        return i
    