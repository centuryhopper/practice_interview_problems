class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        seen = set()
        globalLst = []
        # region helper

        def getSubsets(nums, path, cur) -> None:
            nonlocal globalLst, seen
            if cur == len(nums):
                path = sorted(path)
                t = tuple(path)
                if t in seen:
                    return
                globalLst.append(path)
                seen.add(t)
                return
            # take the current value at cur
            getSubsets(nums, path+[nums[cur]], cur+1)

            # don't take the current value at cur
            getSubsets(nums, path, cur+1)
        # endregion
        getSubsets(nums, [], 0)
        return globalLst


# region online optimized solution
# class Solution:
#     def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

#         nums.sort()

#         ans = []
#         self.backtrack([], nums, 0, ans)
#         return ans

#     def backtrack(self, curr, nums, idx, ans):
#         ans.append(curr[:])
#         if idx >= len(nums):
#             return
#         for i in range(idx, len(nums)):
#             if i > idx and nums[i] == nums[i-1]:
#                 continue
#             curr.append(nums[i])
#             self.backtrack(curr, nums, i + 1, ans)
#             curr.pop()

# endregion
