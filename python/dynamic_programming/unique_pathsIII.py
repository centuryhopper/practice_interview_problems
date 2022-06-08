class Solution:
    def __init__(self):
        # cnts total number of zeroes before traversal starts
        self.zeroes = 0
        # cnt the number of zeroes traversed (both variables should be equal upon reaching the ending square for a successful return call)
        # negative -1 because we also count the start position, which is a 1. This way we account for that
        self.cntZeroes = -1

    # i and j should start at the starting square
    def dfs(self, grid, i, j) -> int:
        # error checks and base cases
        m,n = len(grid), len(grid[0])
        if i >= m or i < 0 or j < 0 or j >= n:
            return 0
        # don't go on a bread crumb
        if grid[i][j] == '.':
            return 0
        if grid[i][j] == -1:
            return 0
        if grid[i][j] == 2 and self.cntZeroes == self.zeroes:
            return 1
        # can't continue DFSing on this path if we haven't seen all zeroes prior
        if grid[i][j] == 2:
            return 0

        cnt = 0
        # always have four choices at each square
        for x in range(4):
            tmp = grid[i][j]
            grid[i][j] = '.'
            self.cntZeroes += 1
            # up
            if x == 0:
                cnt += self.dfs(grid,i+1,j)
            # down
            if x == 1:
                cnt += self.dfs(grid,i-1,j)
            # left
            if x == 2:
                cnt += self.dfs(grid,i,j-1)
            # right
            if x == 3:
                cnt += self.dfs(grid,i,j+1)
            # undo state changes
            self.cntZeroes -= 1
            grid[i][j] = tmp
        return cnt

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x, y = -1,-1
        m,n = len(grid), len(grid[0])
        # find starting square position and dfs in all four directions
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x,y = i,j
                if grid[i][j] == 0:
                    self.zeroes+=1

        cnt = self.dfs(grid,x,y)

        return cnt




