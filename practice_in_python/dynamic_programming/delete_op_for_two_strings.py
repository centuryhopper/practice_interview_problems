class Solution:


    # levenshtein distance w/o replace method
    def minDistance(self, w1: str, w2: str) -> int:
        m,n = len(w1), len(w2)
        # preprocess dp array
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # min among left, and top, respectively
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
        # print(dp)
        return dp[m][n]



# slight optimization in my solution with preprocessing the dp array:
# class Solution:
#     def minDistance(self, w1: str, w2: str) -> int:
#         m,n = len(w1), len(w2)
#         # preprocess dp array
#         dp = [[i for i in range(n+1)] for _ in range(m+1)]
#         for i in range(m+1):
#             dp[i][0] = i

#         # print(dp)

#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if w1[i-1] == w2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     # min among left, and top, respectively
#                     dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
#         # print(dp)



#         return dp[m][n]







# class Solution:
#     def minDistance(self, w1: str, w2: str) -> int:
#         m,n = len(w1), len(w2)
#         # preprocess dp array
#         dp = [[0]*(n+1) for _ in range(m+1)]
#         for i in range(m+1):
#             dp[i][0] = i
#         for i in range(n+1):
#             dp[0][i] = i

#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if w1[i-1] == w2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     # dp[i-1][j-1] is for replace operation
#                     # if replace operation is not allowed, then simply do
#                     # dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1 instead
#                     # min among left, upper left diagonal, and top, respectively
#                     dp[i][j] = min(min(dp[i][j-1],dp[i-1][j-1]), dp[i-1][j]) + 1
#         print(dp)



        # return dp[m][n]