from typing import List


class Solution:
    '''
    [1,2,3,4,5,6,7,8,9]


    1,2,3
    4,5,6
    7,8,9


    [[1]] 100
    [[1],[2],[3],[4],[7],[6],[5]]
    23


    '''


    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        lst = [num for row in grid for num in row]
        # print(lst)
        x = 0
        for i in range(m):
            for j in range(n):
                if x-k < 0:
                    res = lst[(x-k+(m*n)) % (m*n)]
                else:
                    res = lst[(x-k) % (m*n)]

                grid[i][j] = res
                x+=1
        return grid




