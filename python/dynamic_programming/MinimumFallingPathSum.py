class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        # will cache the most optimal path at every index
        dp = [[math.inf]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = mat[0][i]
        for i in range(1,n):
            for j in range(n):
                topleft = top = topright = math.inf
                # avoid going out of bounds on the left edge
                if j > 0:
                    topleft = dp[i-1][j-1]
                top = dp[i-1][j]
                # avoid going out of bounds on the right edge
                if j < n-1:
                    topright = dp[i-1][j+1]
                dp[i][j] = min(topleft+mat[i][j],top+mat[i][j],topright+mat[i][j])
#         for row in dp:
#             print(row)
        
        return min(dp[-1])
                
        
