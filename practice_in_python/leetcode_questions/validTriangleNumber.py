class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # the number to search for must be less than the targetSum
        def binarySearch(nums,lo,hi,targetSum) -> int:
            while lo <= hi:
                mid = (lo+hi)//2
                # good number
                if nums[mid] < targetSum:
                    lo = mid+1
                else:
                    if hi == mid: break
                    hi = mid
            return lo
            
        n = len(nums)
        if n < 3: return 0
        
        # sort array
        nums.sort()
        cnt = 0
        # then pick two numbers, then binary search for the third one
        for i in range(n-2):
            for j in range(i+1,n-1):
                idx = binarySearch(nums,j+1,n-1,nums[i]+nums[j])
                # print((i,j,idx),end=' ')
                cnt += (idx - 1) - j
            # print()
        
        return cnt