class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def rec(lst, i, up, down):
            # done with loop so return
            if i >= len(lst):
                return max(up, down)
            # we just decreased, so up = down + 1
            if lst[i] < lst[i-1]:
                return rec(lst, i+1, down+1, down)
            # we just increased, so down = up + 1
            if lst[i] > lst[i-1]:
                return rec(lst, i+1, up, up+1)
            # don't count the ones that are equal
            return rec(lst,i+1,up,down)
        if len(nums) == 1: return 1
        return rec(nums, 1, 1, 1)