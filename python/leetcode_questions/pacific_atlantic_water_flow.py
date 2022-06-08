class Solution:
    def can_dfs(self, is_p, mat, i, j, prev) -> bool:
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
            return False
        if mat[i][j] == '*' or prev < mat[i][j]:
            return False
        # pacific
        if is_p:
            if i == 0 or j == 0:
                return True
        # atlantic
        else:
            if i == len(mat) - 1 or j == len(mat[0]) - 1:
                return True
        down, up, left, right = False, False, False, False
        tmp = mat[i][j]
        # mark as visited
        mat[i][j] = '*'
        down |= self.can_dfs(is_p, mat, i+1, j, tmp)
        if down:
            # undo state change
            mat[i][j] = tmp
            return True
        right |= self.can_dfs(is_p, mat, i, j+1, tmp)
        if right:
            # undo state change
            mat[i][j] = tmp
            return True
        up |= self.can_dfs(is_p, mat, i-1, j, tmp)
        if up:
            # undo state change
            mat[i][j] = tmp
            return True
        left |= self.can_dfs(is_p, mat, i, j-1, tmp)
        if left:
            # undo state change
            mat[i][j] = tmp
            return True
        # undo state change
        mat[i][j] = tmp
        return False

    def pacificAtlantic(self, mat: List[List[int]]) -> List[List[int]]:
        # deal with empty matrix
        if not mat or len(mat) == 0 or len(mat[0]) == 0: return []
        m = len(mat)
        n = len(mat[0])
        print(f'{m} x {n}')
        lst = []
        for i in range(m):
            for j in range(n):
                cur = mat[i][j]
                if self.can_dfs(True,mat,i,j,cur) and self.can_dfs(False,mat,i,j,cur):
                    lst.append([i,j])
                # print(mat[i][j], end=' ')
            # print()
        return lst






















class Solution:
    def can_dfs_to_P(self, mat, i, j, curHeight) -> bool:
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
            return False
        if curHeight < 0:
            return False
        if i == 0 or j == 0:
            return True

        down, up, left, right = False, False, False, False
        if i + 1 < len(mat):
            down = self.can_dfs_to_P(mat, i+1, j, curHeight - mat[i+1][j])
        if j + 1 < len(mat[0]):
            right = self.can_dfs_to_P(mat, i, j+1, curHeight - mat[i][j+1])
        up = self.can_dfs_to_P(mat, i-1, j, curHeight - mat[i-1][j])
        left = self.can_dfs_to_P(mat, i, j-1, curHeight - mat[i][j-1])
        return up or down or left or right

    def can_dfs_to_A(self, mat, i, j, curHeight) -> bool:
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
            return False
        if curHeight < 0:
            return False
        if i == len(mat) - 1 or j == len(mat[0]) - 1:
            return True

        down, up, left, right = False, False, False, False
        if i - 1 >= 0:
            up = self.can_dfs_to_A(mat, i-1, j, curHeight - mat[i-1][j])
        if j - 1 >= 0:
            left = self.can_dfs_to_A(mat, i, j-1, curHeight - mat[i][j-1])
        down = self.can_dfs_to_A(mat, i+1, j, curHeight - mat[i+1][j])
        right = self.can_dfs_to_A(mat, i, j+1, curHeight - mat[i][j+1])
        return up or down or left or right


    def pacificAtlantic(self, mat: List[List[int]]) -> List[List[int]]:
        # deal with empty matrix???
        m = len(mat)
        n = len(mat[0])
        lst = []
        for i in range(m):
            for j in range(n):
                cur = mat[i][j]
                if self.can_dfs_to_A(mat,i,j,cur) and self.can_dfs_to_P(mat,i,j,cur):
                    lst.append([i,j])
                print(mat[i][j], end=' ')
            print()
        return lst


