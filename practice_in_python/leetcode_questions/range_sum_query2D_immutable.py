class NumMatrix:
    # Time: O(m*n)
    def __init__(self, mat: list[list[int]]):
        self.mat = mat
        m, n = len(mat), len(mat[0])
        self.dp = [[0]*n for _ in range(m)]
        self.dp[0][0] = mat[0][0]
        # seed first row only if there's more than one column
        for i in range(1, n):
            self.dp[0][i] = self.dp[0][i-1] + self.mat[0][i]

        # seed first column only if there's more than one row
        for i in range(1, m):
            self.dp[i][0] = self.dp[i-1][0] + self.mat[i][0]

        # fill in rest of table based on seeded values
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - \
                    self.dp[i-1][j-1]+self.mat[i][j]
        # for l in self.dp:
        #     print(l)

    # Time O(1)
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # avoid index out of bounds checks
        top = self.dp[r1-1][c2] if r1 > 0 else 0
        left = self.dp[r2][c1-1] if c1 > 0 else 0
        topleft = 0
        if r1 > 0 and c1 > 0:
            topleft = self.dp[r1-1][c1-1]
        return self.dp[r2][c2] - top - left + topleft

        # brute force way
        # res = 0
        # # for i in range(r1, r2+1):
        # #     for j in range(c1, c2+1):
        # #         res+=self.mat[i][j]
        # return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)





if __name__ == '__main__':
    # obj = NumMatrix([[-4,-5]])
    # a = obj.sumRegion(0, 0, 0, 0)
    # print(a)
    # a = obj.sumRegion(0,0,0,1)
    # print(a)
    # a = obj.sumRegion(0,1,0,1)
    # print(a)

    obj = NumMatrix([[1],[-7]])
    a = obj.sumRegion(0, 0, 0, 0)
    print(a)

    a = obj.sumRegion(1,0,1,0)
    print(a)

    a = obj.sumRegion(0,0,1,0)
    print(a)


# brute force approach O(1) space but hella slow when calling sumRegion()
# multiple times on large sub-matrices
# class NumMatrix:
#     def __init__(self, mat: List[List[int]]):
#         self.mat = mat

#     def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:

#         res = 0
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 res+=self.mat[i][j]
#         return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
