from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # return the distance to the nearest zero
        def bfs(mat, i, j) -> int:
            q = deque([(i, j)])
            visited = set()
            m = len(mat)
            n = len(mat[0])
            one, two = 0, 0
            while q:
                x, y = q.popleft()
                # find a zero and return the distance
                if mat[x][y] == 0:
                    one, two = x, y
                    break
                visited.add((x, y))
                for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if a < 0 or a >= m or b < 0 or b >= n or (a, b) in visited:
                        continue
                    q.append((a, b))
            return abs(two-j) + abs(one-i)

        m, n = len(mat), len(mat[0])
        ret = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                ret[i][j] = bfs(mat, i, j)
        return ret
