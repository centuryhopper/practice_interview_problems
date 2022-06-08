
class Solution:
    def __init__(self):
        self.cnt = 0

    def totalNQueens(self, n: int) -> int:
        def updateArrays(vert, ld, rd, neg, rowNum, colNum, val) -> None:
            vert[colNum] += val
            rd[rowNum + colNum] += val
            if colNum - rowNum > 0:
                ld[colNum - rowNum] += val
            else:
                neg[abs(colNum - rowNum)] += val

        def notPlaceable(vert, ld, rd, neg, rowNum, colNum) -> bool:
            # if rowNum == 4:
            #     print(rowNum, colNum)
            #     print('ld:', ld)
            #     print('rd:', rd)
            #     print('vert:', vert)
            if colNum - rowNum > 0:
                if ld[colNum - rowNum] > 0:
                    return True
            elif neg[abs(colNum - rowNum)] > 0:
                return True
            return vert[colNum] > 0 or rd[rowNum + colNum] > 0

        def solve(n, rowNum, vert, ld, rd, neg) -> None:
            # base case:
            # completed the board
            if rowNum > n:
                # we need a separate reference so that these don't get deleted
                self.cnt += 1
                return
            # we should always have n choices to choose to play the queen per row
            for colNum in range(1, n+1):
                if notPlaceable(vert, ld, rd, neg, rowNum, colNum):
                    continue
                # modify all three arrays for proper future queen placements
                updateArrays(vert, ld, rd, neg, rowNum, colNum, 1)

                # make a choice on the next row
                solve(n, rowNum+1, vert, ld, rd, neg)

                updateArrays(vert, ld, rd, neg, rowNum, colNum, -1)

        if n == 1:
            return 1
        # create board
        # board = [[0]*n for _ in range(n)]
        # wont need a horizontal check because we can restrict ourselves to place
        # one queen per row

        # frequency arrays
        # for vertical checks
        vert = [0]*(n+1)

        # right diagonal (from down to up)
        # row + column
        rd = [0]*(2*n+1)

        # left diagonal (from up to down)
        # column - row
        ld = [0]*(2*n+1)

        # left diagonal (from up to down)
        # such that row number > column number
        neg = [0]*(2*n+1)

        solve(n, 1, vert, ld, rd, neg)

        return self.cnt
