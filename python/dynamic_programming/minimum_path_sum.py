import sys
from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        @lru_cache(None)
        def rec(i, j):
            # goal
            if i == m-1 and j == n-1:
                return grid[i][j]
            # out of bounds
            if i == m or j == n:
                return sys.maxsize
            # any other case
            return grid[i][j] + min(rec(i+1,j),rec(i,j+1))
        
        
        return rec(0,0)
        
