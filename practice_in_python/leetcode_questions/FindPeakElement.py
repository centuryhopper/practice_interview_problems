

#region O(log n) solution using binary search
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        lo = 0
        hi = n-1
        # since input size is up to 1000,
        # integer overflow shouldn't be an issue using this
        # formula for languages like c++ and java
        mid = 0
        # should be lo<=hi instead of lo<hi, otherwise a testcase like
        # [6,5,4,3,2,3,2] will return 1 instead of 0
        while lo<=hi:
            mid = (lo+hi)//2
            cur = nums[mid]
            # bounds check when checking neighbors
            if mid==0:
                if cur > nums[mid+1]:
                    break
                return mid+1
            if mid == n-1:
                if cur > nums[mid-1]:
                    break
                return mid-1
            if nums[mid-1] > cur:
                hi = mid-1
            elif nums[mid+1] > cur:
                lo = mid+1
            # could just say else but I wanted clarity
            elif nums[mid+1] < cur > nums[mid-1]:
                break
        return mid
#endregion

