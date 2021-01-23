from collections import deque


class Solution:

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        d = deque()
        max_number_allowed_to_pop = len(nums) - k

        for i, num in enumerate(nums):

            # stack is not empty, current element is less than the peek()
            # and we haven't exhausted our pop limit
            while d and num < d[-1] and max_number_allowed_to_pop > 0:
                max_number_allowed_to_pop -= 1
                d.pop()

            d.append(num)

        # print(d)

        return list(d)[:k]


# keep popping until the list
# # is empty or the peeked element is
# # smaller than num
# # makes sure we still have at least k elements to choose
#             if d and num < d[-1]:

#                 # if there aren't enough elements available
#                 if len(nums) - i < k:

#                     # keep popping until d is of size k - 1
#                     while len(d) > k - 1 and num < d[-1]:
#                         d.pop()

#                 # there are enough items available
#                 else:
#                     while d and num < d[-1]:
#                         d.pop()
