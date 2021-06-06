class Solution:

    def __init__(self):
        self.cnt = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j) -> None:
            # bounds check
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            # traversible check
            if grid[i][j] == 0 or grid[i][j] == 'X':
                return
            # mark as visited
            grid[i][j] = 'X'
            # globally count it
            self.cnt += 1
            # up down left right, respectively
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)

        maxVal = 0
        m, n = len(grid), len(grid[0])
        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    dfs(grid, a, b)
                    maxVal = max(maxVal, self.cnt)
                    # reset the cnt for potential future use
                    self.cnt = 0
        return maxVal


'''
online iterative solution

class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
'''
