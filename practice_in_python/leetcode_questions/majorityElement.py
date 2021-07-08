class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        candidate = nums[0]
        cnter = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                cnter += 1
            else:
                cnter -= 1
            if cnter == 0:
                cnter += 1
                candidate = nums[i]
        return candidate
