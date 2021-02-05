class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 2:
            nums.reverse()
            return
        n = len(nums)
        cur = n - 2

        while cur >= 0 and nums[cur] >= nums[cur + 1]:
            cur -= 1
        if cur == -1:
            nums.reverse()
            return
        for i in range(n-1, cur, -1):
            if nums[i] > nums[cur]:
                nums[i], nums[cur] = nums[cur], nums[i]
                break

        # reverse everything after cur
        nums[cur+1:] = reversed(nums[cur+1:])
