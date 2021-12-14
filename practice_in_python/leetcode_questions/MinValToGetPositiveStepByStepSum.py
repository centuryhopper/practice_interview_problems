class Solution:
    '''
    [-3, 2, -3, 4, 2]
     -3 -1 -4  0  2

    [1, 2]
     1  3

    [1, -2, -3]
     1  -1  -4
    '''
    def minStartValue(self, nums: List[int]) -> int:
        minVal = float('inf')
        runningSum = 0
        for num in nums:
            runningSum+=num
            minVal = min(minVal,runningSum)

        # this means all numbers are non-negative
        if minVal >= 1:
            return 1

        # negative values exist
        return 1 - minVal
