class Solution:

    # cheating way (would fail at a real interview)
    # O(n log n) time and O(n) space
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()

        # keep a global max cnt for tracking consecutive sequences
        globalCnt = 1
        # have a local cnt as well but update the global max everytime just before the
        # local cnt resets
        localCnt = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                localCnt += 1
            else:
                globalCnt = max(globalCnt, localCnt)
                localCnt = 1
        globalCnt = max(globalCnt, localCnt)

        return globalCnt



# O (n) time and space solution
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums: return 0

#         st = set(nums)
#         best = 0
#         currentStreak = 1
#         for num in nums:
#             # find the smallest consecutive element
#             # and build from there
#             currentStreak = 1
#             if num - 1 in st:
#                 continue
#             # find the longest streak
#             while num + 1 in st:
#                 num+=1
#                 # remove it so that we only count it once
#                 st.remove(num)
#                 currentStreak+=1


#             best = max(best, currentStreak)

#         return max(best, currentStreak)







