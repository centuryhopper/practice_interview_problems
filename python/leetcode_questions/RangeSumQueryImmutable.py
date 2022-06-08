

class NumArray:
    def __init__(self, nums: List[int]):
        # build sum array
        n = len(nums)
        self.lst = [0]*n
        self.lst[0] = nums[0]
        for i in range(1,n):
            self.lst[i] = self.lst[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.lst[right] - self.lst[left-1] if left > 0 else self.lst[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)