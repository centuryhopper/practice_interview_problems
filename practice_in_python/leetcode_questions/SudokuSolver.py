
class Solution:
    # region failed attempt
    # def solveSudoku(self, board: list[list[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     def isPlacementValid(board, i, j, value) -> bool:
    #         nonlocal m, n
    #         # check rows (vary i, fix j)
    #         for x in range(m):
    #             val = board[x][j]
    #             if val == '.':
    #                 continue
    #             if val == value:
    #                 return False

    #         # check cols (fix i, vary j)
    #         for x in range(n):
    #             val = board[i][x]
    #             if val == '.':
    #                 continue
    #             if val == value:
    #                 return False

    #         x = y = 0
    #         if 3 <= i < 6:
    #             x = 3
    #         elif 6 <= i < 9:
    #             x = 6
    #         if 3 <= j < 6:
    #             y = 3
    #         elif 6 <= j < 9:
    #             y = 6

    #         for a in range(x, x+3):
    #             for b in range(y, y+3):
    #                 val = board[a][b]
    #                 if val == '.':
    #                     continue
    #                 if val == value:
    #                     return False

    #         return True

    #     # true when a solution was found
    #     # false when all possibilities have been exhausted
    #     def rec(board) -> None:
    #         nonlocal m, n
    #         for x in range(9):
    #             for y in range(9):
    #                 # skip already filled in numbers
    #                 if board[x][y] != '.':
    #                     continue
    #                 # 9 possible numbers for each blank spot
    #                 for k in range(1, 10):
    #                     if isPlacementValid(board, x, y, k):
    #                         board[x][y] = f'{k}'
    #                         rec(board)
    #                         # undo state change for other calls
    #                         board[x][y] = '.'

    #     m, n = len(board), len(board[0])

    #     rec(board)
    # endregion

    # region my complete solution
    @staticmethod
    def solveSudoku(board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isPlacementValid(board, i, j, value) -> bool:
            # check rows (vary i, fix j)
            for x in range(9):
                if board[x][j] == value:
                    return False
            # check cols (fix i, vary j)
            for x in range(9):
                if board[i][x] == value:
                    return False
            s = (i//3) * 3
            e = (j//3) * 3
            for a in range(3):
                for b in range(3):
                    if board[s+a][e+b] == value:
                        return False
            return True

        def findEmpty(board) -> tuple[int, int]:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.' or board[i][j] == '0':
                        return (i, j)
            return None

        # true when a solution was found
        # false when all possibilities have been exhausted
        def rec(board) -> bool:
            # O(n^2) base case check
            vals = findEmpty(board)
            # no more empty slots
            # so we're done
            if not vals:
                return True
            x, y = vals
            for k in range(1, 10):
                if isPlacementValid(board, x, y, f'{k}'):
                    board[x][y] = f'{k}'
                    if rec(board):
                        return True
                    # undo state change for other calls
                    board[x][y] = '.'
            return False
        rec(board)
    # endregion


if __name__ == '__main__':
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
    #                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
    #          [6, 0, 0, 0, 7, 5, 0, 0, 9],
    #          [0, 0, 0, 6, 0, 1, 0, 7, 8],
    #          [0, 0, 7, 0, 4, 0, 2, 6, 0],
    #          [0, 0, 1, 0, 5, 0, 9, 3, 0],
    #          [9, 0, 4, 0, 6, 0, 0, 0, 5],
    #          [0, 7, 0, 3, 0, 0, 0, 1, 2],
    #          [1, 2, 0, 0, 0, 7, 4, 0, 0],
    #          [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    board = [[3, 0, 0, 0, 0, 1, 9, 0, 0],
             [0, 0, 0, 0, 7, 0, 4, 0, 0],
             [1, 0, 0, 4, 2, 0, 0, 0, 0],
             [5, 3, 1, 0, 0, 0, 0, 7, 0],
             [0, 4, 9, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 6, 0, 0, 0, 0, 0],
             [0, 9, 0, 0, 0, 2, 0, 5, 7],
             [2, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 9, 0, 0, 8, 0]]
    for i, row in enumerate(board):
        board[i] = list(map(lambda elem: str(elem), row))
    print('before:')
    for row in board:
        print(row)
    print()
    Solution.solveSudoku(board)
    print('after:')
    for row in board:
        print(row)
