

class Solution:
    # n = 6 [1, 3, 5, 7, 9, 11] => 9

    def minOperations(self, n: int) -> int:
        # if n is even then add every odd index
        # if n is odd then add every even index
        return sum(i for i in range(0, n, 2)) if n & 1 else sum(i for i in range(1, n, 2))




        # brute force
        # lst = [(2 * i) + 1 for i in range(n)]
        # print(lst)
        # target = n
        # print(target)
        # i, j = 0, n-1
        # cntOps = 0
        # while i < j:
        #     if lst[j] != lst[i]:
        #         cntOps+=1
        #         lst[j]-=1
        #         lst[i]+=1
        #     else:
        #         i+=1
        #         j-=1
        # return cntOps








# more optimized solution
# class Solution:
#     def minOperations(self, n: int) -> int:
#         x = n // 2
#         return x * (n-x)