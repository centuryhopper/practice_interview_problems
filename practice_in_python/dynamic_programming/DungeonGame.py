class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        mat = dungeon
        m, n = len(mat), len(mat[0])
        dp = [[0]*n for _ in range(m)]
        # work backwards
        # seed the bottom right
        dp[m-1][n-1] = 1 + abs(mat[m-1][n-1]) if mat[m-1][n-1] < 0 else 1
        # preprocess last row
        for i in range(n-2, -1, -1):
            dp[m-1][i] = dp[m-1][i+1] + \
                abs(mat[m-1][i]) if mat[m -
                                        1][i] < 0 else dp[m-1][i+1] - mat[m-1][i]
            if dp[m-1][i] <= 0:
                dp[m-1][i] = 1
        # debug check
        # for row in dp:
        #     print(row)

        # preprocess last column
        for i in range(m-2, -1, -1):
            dp[i][n-1] = dp[i+1][n-1] + \
                abs(mat[i][n-1]) if mat[i][n -
                                           1] < 0 else dp[i+1][n-1] - mat[i][n-1]
            if dp[i][n-1] <= 0:
                dp[i][n-1] = 1
        # debug check
        # for row in dp:
        #     print(row)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cur = mat[i][j]
                if cur > 0:
                    dp[i][j] = min(dp[i+1][j] - cur, dp[i][j+1] - cur)
                else:
                    dp[i][j] = min(dp[i+1][j] + abs(cur),
                                   dp[i][j+1] + abs(cur))
                if dp[i][j] <= 0:
                    dp[i][j] = 1

        # debug check
        # for row in dp:
        #     print(row)
        return dp[0][0]
