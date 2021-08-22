


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        leftToRight = [1]*n
        rightToLeft = [1]*n
        leftToRight[0] = nums[0]
        rightToLeft[0] = nums[n-1]

        for i in range(1, n):
            leftToRight[i] = nums[i] * leftToRight[i -
                                                   1] if leftToRight[i-1] != 0 else nums[i]
            rightToLeft[i] = nums[n-1-i] * rightToLeft[i -
                                                       1] if rightToLeft[i-1] != 0 else nums[n-1-i]

        # print(leftToRight)
        # print(rightToLeft)

        maxVal = float('-inf')
        for i in range(n):
            maxVal = max(maxVal, max(rightToLeft[i], leftToRight[i]))
        return maxVal
