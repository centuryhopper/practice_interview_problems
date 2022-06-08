


#region brute force
# class Solution:
#     def countBits(self, n: int) -> list[int]:
#         def count(n) -> int:
#             cnt = 0
#             while n > 0:
#                 cnt+=1 if (n&1) else 0
#                 n>>=1
#             return cnt
#         lst = []
#         for i in range(n+1):
#             lst.append(count(i))
#         return lst
#endregion
        