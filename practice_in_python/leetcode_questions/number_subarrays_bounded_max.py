
# region O(n) time solution
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
        total,s,window = 0,0,0
        for i, num in enumerate(nums):
            # too small
            if num < l:
                # add what's currently in window to our total
                total += window
            # in range
            elif l <= num <= r:
                window = (i - s + 1)
                total += window
            # too big
            elif num > r:
                # need to start a new window
                window = 0
                # reset the two pointers
                s = i + 1
        return total
# endregion


# region n^2 runtime
# class Solution:
#     def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
#         total = 0
#         for i in range(len(nums)):
#             start = nums[i]
#             if start > r:
#                 continue
#             cnt = 0
#             if l <= start <= r:
#                 cnt += 1
#             curMax = start
#             for j in range(i+1, len(nums)):
#                 if nums[j] > r:
#                     break
#                 curMax = max(curMax, nums[j])
#                 if cnt > 0 or l <= curMax <= r:
#                     cnt += 1
#             total += cnt

#         return total
# endregion
