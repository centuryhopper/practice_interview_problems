class Solution:
    '''
    [1,1,2,2,3]

    # based on the problem statement, all input sizes must be odd
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # cheating way:
        # return collections.Counter(nums).most_common()[-1][0]

        n = len(nums)
        lo,hi = 0, n-1
        while lo < hi:
            mid = lo + ((hi-lo) // 2)
            # discard the left half iff nums[mid] == nums[mid+1] for odd mids and iff nums[mid] == nums[mid+1] for even mids
            # otherwise, discard the right half
            if mid % 2 == 1 and nums[mid] == nums[mid-1]:
                lo=mid+1
            elif mid % 2 == 0 and nums[mid] == nums[mid+1]:
                lo=mid+1
            else:
                hi=mid
        return nums[lo]




