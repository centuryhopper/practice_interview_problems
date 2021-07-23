from functools import reduce

#region optimized solution

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        summ = 0
        def rec(nums, path, i) -> None:
            nonlocal summ
            if i == len(nums):
                summ+=path
                return
            # recurse on path with current value
            rec(nums,path^nums[i],i+1)
            # recurse on path without current value
            rec(nums,path,i+1)
        rec(nums,0,0)
        return summ


#endregion


#region not as optimized solution

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        lst = []
        def rec(nums, path, i) -> None:
            nonlocal lst
            # all other success case
            if i == len(nums):
                lst.append(reduce(lambda x,y: x^y, path, 0))
                return
            # recurse on path with current value
            rec(nums,path+[nums[i]],i+1)
            # recurse on path without current value
            rec(nums,path,i+1)
        rec(nums,[],0)
        return sum(lst)
#endregion