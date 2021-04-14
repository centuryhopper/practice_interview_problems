class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        def vp(mat: List[List[int]]) -> None:
            for lst in mat:
                for num in lst:
                    print(num, end=" ")
                print()
        rB = 0
        rE = n - 1
        cB = 0
        cE = n - 1
        cnt = 1

        # n x n matrix
        mat = []
        for i in range(n):
            mat.append([])
            for j in range(n):
                mat[i].append(0)

        while rB <= rE and cB <= cE:
            print()

            if (rB == rE and cB == cE):
                if (n % 2 == 1):
                    mat[rB][rB] = n ** 2
                    break

            for i in range(cB, cE):
                mat[rB][i] = cnt
                cnt += 1
            vp(mat)

            for i in range(rB, rE):
                mat[i][cE] = cnt
                cnt += 1
            vp(mat)
            for i in range(cE, cB, -1):
                mat[rE][i] = cnt
                cnt += 1
            vp(mat)

            for i in range(rE, rB, -1):
                mat[i][cB] = cnt
                cnt += 1
            vp(mat)

            rB += 1
            cB += 1
            rE -= 1
            cE -= 1
        return mat
