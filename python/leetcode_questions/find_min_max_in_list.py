import sys

class Solution():
    """
    Given an array, lst, find the
    smallest and largest number in lst
    """
    def get_min_max(self, lst: list[int]) -> (int, int):

        minimum = float('inf')
        maximum = float('-inf')

        # brute force approach
        # for num in lst:
        #     minimum = min(minimum, num)
        #     maximum = max(maximum, num)

        # return (minimum, maximum)

        # optimized minimum number of comparisons
#         for i in range(1, len(lst), 2)

# s = Solution()

# print(s.get_min_max([7,3,5,9,2,4]))

# print(float('-inf'))
# print(float('inf'))
myInt = 1
print(sys.getsizeof(myInt))
