
class Solution:
    def numIslands(self, a: List[List[str]]) -> int:

        def mark(a: List[List[str]], r: int, c: int):
            a[r][c] = '*'

        #  check bounds function
        def isInBounds(row: int, col: int, rowLen: int, colLen: int) -> bool:
            return (row < rowLen and row >= 0) and (col < colLen and col >= 0)

        # breadth-first search algo
        def bfs(a: List[List[str]], r: int, c: int):
            if (not isInBounds(r, c, len(a), len(a[0]))) or (a[r][c] == '*' or a[r][c] == '0'): return

            mark(a, r, c)

            # up
            bfs(a, r - 1, c)

            # down
            bfs(a, r + 1, c)

            # left
            bfs(a, r, c - 1)

            # right
            bfs(a, r, c + 1)

        nC = len(a[0])
        if nC == 0: return 0
        nR = len(a)

        cnt = 0

        for c in range(nC):
            if a[0][c] == '1':
                mark(a, 0, c)
                cnt += 1

                # down and right
                bfs(a, 1, c)
                bfs(a, 0, c + 1)
                #print(f"first row's cnt: {cnt}")

            if a[nR - 1][c] == '1':
                mark(a, nR - 1, c)
                cnt += 1

                # up and right
                bfs(a, nR - 2, c)
                bfs(a, nR - 1, c + 1)
                #print(f"last row's cnt: {cnt}")

        for r in range(nR):
            if a[r][0] == '1':
                mark(a, r, 0)
                cnt += 1

               # right and down
                bfs(a, r, 1)
                bfs(a, r + 1, 0)
                #print(f"first column's cnt: {cnt}")

            if a[r][nC - 1] == '1':
                mark(a, r, nC - 1)
                cnt += 1

                # left and down
                bfs(a, r, nC - 2)
                bfs(a, r + 1, nC - 1)
                #print(f"last column's cnt: {cnt}")

        for i in range(nR):
            for j in range(nC):
               # print(a[i][j] + ' ', end='')
                if a[i][j] == '1':
                    cnt += 1
                    # DFS up, down left, and right, respectively
                    bfs(a, i - 1, j)
                    bfs(a, i + 1, j)
                    bfs(a, i, j - 1)
                    bfs(a, i, j + 1)
            #print()
        return cnt






# class Solution:
#     def numIslands(self, a: List[List[str]]) -> int:

#         def mark(a: List[List[str]], r: int, c: int):
#             a[r][c] = None

#         # check bounds function
#         def isInBounds(row: int, col: int, rowLen: int, colLen: int) -> bool:
#             return (row < rowLen and row >= 0) and (col < colLen and col >= 0)

#         # Depth-first search algo
#         def DFS(a: List[List[str]], r: int, c: int):
#             if (not isInBounds(r, c, len(a), len(a[0]))) or (a[r][c] == None or a[r][c] == '0'): return

#             mark(a, r, c)

#             # up
#             DFS(a, r - 1, c)

#             # down
#             DFS(a, r + 1, c)

#             # left
#             DFS(a, r, c - 1)

#             # right
#             DFS(a, r, c + 1)

#         nC = len(a[0])
#         if nC == 0: return 0
#         nR = len(a)

#         cnt = 0

#         for c in range(nC):
#             if a[0][c] == '1':
#                 mark(a, 0, c)
#                 cnt += 1

#                 # down and right
#                 DFS(a, 1, c)
#                 DFS(a, 0, c + 1)
#                 #print(f"first row's cnt: {cnt}")

#             if a[nR - 1][c] == '1':
#                 mark(a, nR - 1, c)
#                 cnt += 1

#                 # up and right
#                 DFS(a, nR - 2, c)
#                 DFS(a, nR - 1, c + 1)
#                 #print(f"last row's cnt: {cnt}")

#         for r in range(nR):
#             if a[r][0] == '1':
#                 mark(a, r, 0)
#                 cnt += 1

#                # right and down
#                 DFS(a, r, 1)
#                 DFS(a, r + 1, 0)
#                 #print(f"first column's cnt: {cnt}")

#             if a[r][nC - 1] == '1':
#                 mark(a, r, nC - 1)
#                 cnt += 1

#                 # left and down
#                 DFS(a, r, nC - 2)
#                 DFS(a, r + 1, nC - 1)
#                 #print(f"last column's cnt: {cnt}")

#         for i in range(1, nR - 1):
#             for j in range(1, nC - 1):
#                # print(a[i][j] + ' ', end='')
#                 if a[i][j] == '1':
#                     cnt += 1
#                     DFS(a, i, j)

#             #print()
#         return cnt