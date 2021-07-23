
#region more optimized
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        # invalid dimensions
        if r*c != m*n: return mat
        new = [[0]*c for _ in range(r)]
        row,col = 0,0
        for i in range(m):
            for j in range(n):
                if col == c:
                    # go to the next row
                    row+=1
                    col=0
                new[row][col] = mat[i][j]
                col+=1
                
        return new
#endregion


#region not as optimized
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         m,n = len(mat), len(mat[0])
#         # invalid dimensions
#         if r*c != m*n: return mat
        
#         # 1-d conversion
#         lst = [0]*(m*n)
#         for i in range(m):
#             for j in range(n):
#                 lst[n*i+j] = mat[i][j]
#         print(lst)
        
#         # 2-d conversion
#         # new = [[0]*c for _ in range(r)]
#         # # print(new)
#         # for i in range(m*n):
#         #     # print(i%r, i//r)
#         #     new[i%r][i//r] = lst[i]
#         new = []
#         idx = 0
#         for i in range(r):
#             new.append([])
#             for _ in range(c):
#                 new[i].append(lst[idx])
#                 idx+=1
                
#         return new
#endregion