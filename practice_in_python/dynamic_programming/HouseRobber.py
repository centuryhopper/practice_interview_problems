class Solution:
    
    '''
    [1,2,3,1]
    [1,2,3+1=4,2+1=3]
    
    [2,7,9,3,1]
    [2,7,9+2=11,10,11+1=12]
    
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        mostMoney = max(dp[0],dp[1])
        for i in range(2,n):
            curBest = 0
            for j in range(i):
                # we cant rob the current house if we robbed the adjacent house (i.e. j == i - 1)
                curBest = max(curBest,dp[j]+nums[i] if j != i - 1 else dp[j])
            dp[i] = curBest
            mostMoney = max(mostMoney,dp[i])
        # print(dp)
        return mostMoney
    
    
    