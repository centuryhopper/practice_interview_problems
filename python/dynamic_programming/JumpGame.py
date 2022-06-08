class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # if n == 1: return True
        dp = [False]*n
        # we can always reach the last index from the last index
        dp[n-1] = True
        for i in range(n-2,-1,-1):
            dp[i] = any((dp[j] for j in range(i+1, min(i+1+nums[i], n))))
        return dp[0]
