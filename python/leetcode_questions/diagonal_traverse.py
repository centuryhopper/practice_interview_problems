
import enum as e
from collections import deque

import enum as e
from collections import deque


class Diagonals(e.Enum):
    up = 1
    down = 2


class Solution:

    def r_out_bounds(self, rows: int, r: int) -> bool:
        return r < 0 or r >= rows

    def c_out_bounds(self, cols: int, c: int) -> bool:
        return c < 0 or c >= cols

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        v: List[int] = []
        d = deque()
        direction = Diagonals.up
        numDiagonals = m + n - 1
        rowVal, colVal = 0, 0
        r, c = rowVal, colVal

        while len(v) < (m * n):

            d.append(matrix[r][c])

            r = r - 1
            c = c + 1

            if (self.r_out_bounds(m, r) or self.c_out_bounds(n, c)):

                # finished with current diagonal
                if direction is Diagonals.up:
                    v.extend(d)
                else:
                    v.extend(reversed(d))
                d.clear()

                if rowVal < m - 1:
                    rowVal += 1
                    colVal = 0
                    r = rowVal
                    c = colVal
                else:
                    colVal += 1
                    c = colVal
                    r = rowVal

                # move to the next diagonal and invert Flag
                direction = Diagonals.up if direction is Diagonals.down else Diagonals.down
        return v


# class Diagonals(e.Enum):
#     up = 1
#     down = 2


# class Solution:

#     def r_out_bounds(self, rows: int, r: int) -> bool:
#         return r < 0 or r >= rows

#     def c_out_bounds(self, cols: int, c: int) -> bool:
#         return c < 0 or c >= cols

#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         if matrix is None or len(matrix) == 0:
#             return []
#         m = len(matrix)
#         n = len(matrix[0])
#         print(f'm: {m}')
#         print(f'n: {n}')
#         v: List[int] = []
#         d = deque()

#         # for lst in matrix:
#         #     for i, num in enumerate(lst):
#         #         print(f'i: {i}, num: {num}')

#         direction = Diagonals.up
#         # print(direction)

#         numDiagonals = m + n - 1
#         rowVal, colVal = 0, 0
#         r, c = rowVal, colVal

#         while len(v) < (m * n):

#             print(f'current rowVal: {rowVal}, current colVal: {colVal}')
#             print(f'appending value at {r},{c}')
#             d.append(matrix[r][c])

#             r = r - 1
#             c = c + 1
#             print(f'next coordinates to potentially get: {r}, {c}')
#             print('-------------')

#             if (self.r_out_bounds(m, r) or self.c_out_bounds(n, c)):

#                 # finished with current diagonal
#                 if direction is Diagonals.up:
#                     v += list(d)
#                 else:
#                     v += reversed(list(d))
#                 d.clear()

#                 if rowVal < m - 1:
#                     rowVal += 1
#                     colVal = 0
#                     r = rowVal
#                     c = colVal
#                 else:
#                     colVal += 1
#                     c = colVal
#                     r = rowVal

#                 # move to the next diagonal and invert Flag
#                 direction = Diagonals.up if direction is Diagonals.down else Diagonals.down

#         print(v)

#         return v


# harder to work with solution (not quite done bc it involves zigzags)
# class Solution:

#     def r_out_bounds(self, rows: int, r: int) -> bool:
#         return r < 0 or r >= rows
#     def c_out_bounds(self, cols: int, c: int) -> bool:
#         return c < 0 or c >= cols

#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         if matrix is None or len(matrix) == 0:
#             return []
#         m = len(matrix)
#         n = len(matrix[0])
#         v : List[int] = []

#         # for lst in matrix:
#         #     for i, num in enumerate(lst):
#         #         print(f'i: {i}, num: {num}')

#         direction = Diagonals.up
#         # print(direction)


#         numDiagonals = m + n - 1
#         rowVal, colVal = 0, 0
#         r = rowVal
#         c = colVal


# #       must add all the values in the matrix
#         while len(v) < (m * n):

#             if (self.r_out_bounds(m, r) or self.c_out_bounds(n, c)):
#                 print('switching diagonal traversing directions')
#                 r = rPrev
#                 c = cPrev

#                 if halfway_reached:
#                     if (direction is Diagonals.down):
#                         c += 1
#                     else:
#                         r += 1
#                 else:
#                     if (direction is Diagonals.down):
#                         r += 1
#                     else:
#                         c += 1

#                 # move to the next diagonal and invert Flag
#                 direction = Diagonals.up if direction is Diagonals.down else Diagonals.down


#             print(f'appending value at {r},{c}')
#             v.append(matrix[r][c])

#             rPrev = r
#             cPrev = c
#             r = r + 1 if direction is Diagonals.down else r - 1
#             c = c - 1 if direction is Diagonals.down else c + 1
#             print(f'next coordinates to potentially get: {r}, {c}')
#             print('-------------')

#         print(v)

#         return v
