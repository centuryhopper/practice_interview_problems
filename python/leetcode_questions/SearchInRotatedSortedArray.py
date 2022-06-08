from typing import List

class Solution:
    '''
    [1,2,4,5,6,7,0]
    [5,6,7,0,1,2,4]
    [0,1,2,4,5,6,7]

    '''
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            # print(nums[mid])
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1 # search in the other subarray
            elif nums[mid] <= nums[hi]:
                if nums[mid] <= target <= nums[hi]:
                    lo=mid+1
                else:
                    hi=mid-1 # search in the other subarray

        return -1