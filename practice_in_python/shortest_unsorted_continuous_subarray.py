class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        lower, upper = float('inf'), float('-inf')

        # find decreasing for lower
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                lower = min(lower, nums[i])

        # find increasing for upper
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                upper = max(upper, nums[i])

        # if both variables have no change, then the array is sorted
        if lower == float('inf') and upper == float('-inf'):
            return 0

        start, end = 0, n-1

        # look for the first value greater than lower bound and that's the starting index
        for i in range(n):
            if nums[i] > lower:
                start = i
                break

        # look for the first value less than upper bound and that's the ending index
        for i in range(n-1, -1, -1):
            if nums[i] < upper:
                end = i
                break

        return end - start + 1
