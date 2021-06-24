from heapq import heappush, heappop, heapify


class Solution:
    # time: O(n^2 log n) because we could in the worst case traverse the entire grid if it's sorted
    # and the minheap takes log n time to manage
    # space: O(n^2) because the visited array could end up storing
    # every value for a sorted grid
    def swimInWater(self, grid: List[List[int]]) -> int:
        # smallest large number needed to get to the
        # destination (unavoidable in terms of finding the optimal path)
        maxVal = 0
        h = []
        heapify(h)
        visited = set()
        cnt = 0
        #region dfs algo with dijkstra's algorithm
        def rec(grid, i, j) -> None:
            nonlocal maxVal, h, visited, cnt
            # bounds check
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            # finish state check
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                maxVal = max(maxVal, grid[i][j])
                return
            # if (i,j) in visited:
            #     return

            maxVal = max(maxVal, grid[i][j])
            # add to visited
            visited.add((i, j))

            # add all reachable paths into our heap
            # up
            if i > 0:
                if (i-1, j) not in visited:
                    heappush(h, (grid[i-1][j], i-1, j))
            # down
            if i < len(grid)-1:
                if (i+1, j) not in visited:
                    heappush(h, (grid[i+1][j], i+1, j))
            # left
            if j > 0:
                if (i, j-1) not in visited:
                    heappush(h, (grid[i][j-1], i, j-1))
            # right
            if j < len(grid[0]) - 1:
                if (i, j+1) not in visited:
                    heappush(h, (grid[i][j+1], i, j+1))

            # cnt += 1
            # print(h,cnt)

            # recurse onto the smallest one
            _, y, z = heappop(h)
            rec(grid, y, z)
        #endregion

        rec(grid, 0, 0)
        return maxVal
