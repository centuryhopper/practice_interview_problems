class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        for i in range(1,n):
            # we either take the optimal profit from the previous
            # day by itself or also add on the possible profit from the current day
            # relative to yesterday
            dp[i] = max(prices[i]-prices[i-1] + dp[i-1],dp[i-1])
        return dp[n-1]
