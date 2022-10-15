
def minDistance(a: str, b: str) -> int:
        m,n = len(a),len(b)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # base cases
        dp[0][0] = 0
        for i in range(1,m+1):
            dp[i][0] = i
        for i in range(1,n+1):
            dp[0][i] = i

        for i in range(1,m+1):
            for j in range(1,n+1):
                # if match then take minimum of left+1,up+1, and diagonal
                # otherwise take the minimum of left+1,up+1, and diagonal+1
                left = dp[i][j-1]
                up = dp[i-1][j]
                diagonal = dp[i-1][j-1]
                if a[i-1] == b[j-1]:
                    dp[i][j] = min(left+1,up+1,diagonal)
                else:
                    dp[i][j] = min(left+1,up+1,diagonal+1)

        for row in dp:
            print(row)

        return dp[m][n]


ans = minDistance("horse", "ros")
#print(ans)
ans = minDistance("acta", "agag")


