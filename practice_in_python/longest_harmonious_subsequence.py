from collections import defaultdict


class Solution:

    # stop loop early when len(nums) - i < current max length subsquence

    #     flag = True

    #     '''finds the longest harmonious subsqeuence for a given value at index i'''
    #     def dfs_subsequence(self, a:list[int], i:int) -> int:
    #         n = len(a)
    #         res = 0
    #         for j in range(i+1, n):
    #             if abs(a[j] - a[i]) == 1:
    #                 Solution.flag = False
    #                 res += 1
    #             elif abs(a[j] - a[i]) == 0:
    #                 res += 1
    #         return res

    #     if len(nums) < 2: return 0
    #         res, n = 0, len(nums)
    #         dfs = self.dfs_subsequence
    #         for i in range(n - 1):
    #             res = max(res, dfs(nums, i))
    #             if res > n - i:
    #                 break

    #         return 0 if Solution.flag else res + 1

    def findLHS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        n = len(nums)
        res = 0
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for key in d.keys():
            if key+1 in d:
                res = max(res, d[key] + d[key+1])
        return res
#     mi, ma = 0, 0
#         while i < n - 1:
#             j = i + 1
#             # we found our max and min value
#             if abs(nums[i] - nums[j]) <= 1:
#                 res += 2
#                 mi, ma = min(nums[i], nums[j]), max(nums[i], nums[j])
#                 # for loop then break
#                 for k in range(j+1,n):
#                     if mi == ma:
#                         if nums[k] == mi or abs(nums[k] - mi) <= 1:
#                             mi, ma = min(mi, nums[k]), max(ma, nums[k])
#                             res += 1
#                     elif ma > mi:
#                         if nums[k] == mi or nums[k] == ma:
#                             mi, ma = min(mi, nums[k]), max(ma, nums[k])
#                             res += 1
#                 break
#             else:
#                 # find our next starting value
#                 i += 1

#         return 0 if mi == ma else res
