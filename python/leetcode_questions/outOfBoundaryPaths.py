from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
        #region brute force

        # def rec(m,n,maxMove,sr,sc) -> int:
            # goal state
#             if sr< 0 or sc < 0 or sr >= m or sc >= n:
#                 # print(sr,sc)
#                 return 1
#             # dead state
#             if maxMove == 0:
#                 # print(sr,sc)
#                 return 0

#             return rec(m,n,maxMove-1,sr-1,sc) + \
#             rec(m,n,maxMove-1,sr+1,sc) + \
#             rec(m,n,maxMove-1,sr,sc-1) + \
#             rec(m,n,maxMove-1,sr,sc+1)
        #endregion

        #region also kinda brute force

        # # find the number of paths given that you must make exactly 'moves' moves
        # def rec(m,n,moves,sr,sc) -> int:
        #     # dead state (can't go down this path)
        #     if (sr < 0 or sc < 0 or sr >= m or sc >= n) and moves > 0:
        #         return 0
        #     # went out of bounds with in exactly 'moves' moves
        #     if (sr < 0 or sc < 0 or sr >= m or sc >= n) and moves == 0:
        #         return 1
        #     # ran out of moves
        #     if moves == 0:
        #         return 0
        #     return rec(m,n,moves-1,sr-1,sc) + rec(m,n,moves-1,sr+1,sc) + rec(m,n,moves-1,sr,sc-1) + rec(m,n,moves-1,sr,sc+1)


        # cnt = 0
        # for i in range(1,maxMove+1):
        #     cnt += rec(m,n,i,sr,sc)
        # return cnt
        #endregion

        #region optimized memoization
        # number of paths given that you must make exactly 'moves' moves
        @cache
        def rec(m,n,moves,sr,sc) -> int:
            # went out of bounds
            if (sr < 0 or sc < 0 or sr >= m or sc >= n):
                return 1
            # ran out of moves
            if moves == 0:
                return 0
            return rec(m,n,moves-1,sr-1,sc) + rec(m,n,moves-1,sr+1,sc) + rec(m,n,moves-1,sr,sc-1) + rec(m,n,moves-1,sr,sc+1)

        mod = 7 + 10**9
        return rec(m,n,maxMove,sr,sc) % mod
        #endregion
