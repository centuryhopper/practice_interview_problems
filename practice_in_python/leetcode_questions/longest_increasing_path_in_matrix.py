

class Solution:
    def rec(self, mat, i, j, prev) -> int:
        # out of bounds
        if i >= len(mat) or i < 0 or j >= len(mat[0]) or j < 0:
            return 0
        # don't keep traversing if previous step's value is at least as large
        if prev >= mat[i][j]:
            return 0
        up = 1 + self.rec(mat,i-1,j, mat[i][j])
        down = 1 + self.rec(mat,i+1,j, mat[i][j])
        left = 1 + self.rec(mat,i,j-1, mat[i][j])
        right = 1 + self.rec(mat,i,j+1, mat[i][j])

        maxPath = max(max(left,right), max(up, down))
        return maxPath

    def rec_memo(self, mat, i, j, prev, memo) -> int:
        # out of bounds
        if i >= len(mat) or i < 0 or j >= len(mat[0]) or j < 0:
            return 0
        # don't keep traversing if previous step's value is at least as large
        if prev >= mat[i][j]:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        up = 1 + self.rec_memo(mat,i-1,j, mat[i][j], memo)
        down = 1 + self.rec_memo(mat,i+1,j, mat[i][j], memo)
        left = 1 + self.rec_memo(mat,i,j-1, mat[i][j], memo)
        right = 1 + self.rec_memo(mat,i,j+1, mat[i][j], memo)
        memo[i][j] = max(max(left,right), max(up, down))
        return memo[i][j]


    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        # memo = [[-1]*n for _ in range(m)]
        # print(memo)
        retVal = 1
        for i in range(m):
            for j in range(n):
                retVal = max(retVal, self.rec(mat,i,j,float('-inf')))
                # print(mat[i][j], end=' ')
            # print()

        return retVal



#online optimized solution
# import functools

# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if not matrix:
#             return 0

#         h = len(matrix)
#         w = len(matrix[0])
#         if not w:
#             return 0

#         # do not cache matrix, not cachable and too big
#         @functools.lru_cache(maxsize=None)
#         def lip(i, j):
#             nbs = []  # neighbours
#             if i > 0: nbs.append((i-1, j))
#             if i < h-1: nbs.append((i+1, j))
#             if j > 0: nbs.append((i, j-1))
#             if j < w-1: nbs.append((i, j+1))

#             maxp = 1
#             for nb in nbs:
#                 if matrix[nb[0]][nb[1]] > matrix[i][j]:
#                     m = lip(nb[0], nb[1])+1
#                     maxp = max(maxp, m)
#             return maxp

#         maxap = 1
#         for i in range(h):
#             for j in range(w):
#                 maxap = max(maxap, lip(i, j))

#         return maxap

#     def longestIncreasingPath(self, matrix):
#         if not matrix or not matrix[0]: return 0
#         M, N = len(matrix), len(matrix[0])
#         @functools.lru_cache(maxsize=None)
#         def dfs(i, j):
#             val = matrix[i][j]
#             return 1 + max(
#                 dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
#                 dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
#                 dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
#                 dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
#         return max(dfs(x, y) for x in range(M) for y in range(N))
