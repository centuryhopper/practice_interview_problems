

# solution to observe
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         smallest_inc = float("inf")
#         smallest_num = float("inf")
#         for i in range(len(nums)):
#             if(nums[i] > smallest_inc): return True
#             if(nums[i] > smallest_num):
#                 smallest_inc = min(smallest_inc, nums[i])
#             smallest_num = min(smallest_num, nums[i])
#         return False

# my solution
class Solution:
    def increasingTriplet(self, As: List[int]) -> bool:


        # error check
        if len(As) < 3: return False

        int_max = 2 ** 31 - 1

        # I may need to make these nullable because
        # otherwise it will fail my custom testcase
        # [1, 2, 2147483647]
        i, j, k = int_max, int_max, int_max

        for a in As:

            # less than or equal instead of strictly less than to avoid
            # duplicates when falling thru to the next else-if branch
            if (a <= i):
                i = a
            elif (a <= j):
                j = a
            elif (a <= k):
                k = a

        if j == int_max or k == int_max: return False

        return i < j and j < k
