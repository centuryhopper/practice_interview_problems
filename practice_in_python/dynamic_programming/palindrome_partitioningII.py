class Solution:
    def minCut(self, s: str) -> int:
        #region helper
        def buildBoolMat(n: int) -> list[list[bool]]:
            dp = [[False]*n for _ in range(n)]
            for i in range(n-1, -1, -1):
                for j in range(i, n):
                    if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                        dp[i][j] = True
            return dp
        #endregion
        if not s:
            return 0
        n = len(s)
        dp = buildBoolMat(n)
        totalCuts = [0]*n
        for j in range(n):
            cut = j
            for i in range(j+1):
                if dp[i][j]:
                    cut = min(cut, 0 if i == 0 else totalCuts[i-1]+1)
            totalCuts[j] = cut
        return totalCuts[n-1]
