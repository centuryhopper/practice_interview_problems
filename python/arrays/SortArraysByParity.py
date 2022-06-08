from typing import List

class Solution:

    '''
    [1,2,3,4,5,6]           [1,2,3,4,5,6]
     i j                     i j (swap!)

    [2,1,3,4,5,6]           [2,1,3,4,5,6]
       i j                     i   j (swap!)

    [2,4,3,1,5,6]           [2,4,3,1,5,6]
         i j                     i   j

    [2,4,3,1,5,6]
         i     j (swap!)

    [2,4,6,1,5,3]
           i j
    ... rinse and repeat etc.

    '''
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] % 2 == 0: continue
            # find a even candidate to swap with nums[i] if possible
            for j in range(i+1,n):
                if nums[j] % 2 == 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    break
        return nums





