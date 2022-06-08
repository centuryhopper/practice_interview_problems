class Solution:

    def isIdealPermutation(self, lst: List[int]) -> bool:
        '''
        time: O(n) in the worst case
        space: O(1) because we don't use any extra data structure to solve our problem
        '''
        if len(lst) <= 2: return True
        # if not lst[0:2] == [0,1] and not lst[0:2] == [1,0]:
        #     return False
        n = len(lst)
        for i in range(n):
            if lst[i] != i - 1 and lst[i] != i and lst[i] != i + 1:
                return False



        return True

    # brute force
#     def isIdealPermutation(self, lst: List[int]) -> bool:
#         if lst == sorted(lst): return True
#         locals, globals = 0,0
#         n = len(lst)

#         for i in range(1, n):
#             if lst[i] < lst[i-1]:
#                 locals += 1
#         for i in range(n-1):
#             for j in range(i, n):
#                 if lst[j] < lst[i]:
#                     globals += 1

#         return locals == globals





# more optimized online solution
# class Solution:
#     def isIdealPermutation(self, A: List[int]) -> bool:
#         for i,v in enumerate(A):
#             if abs(A[i] - i) > 1:
#                 return False
#         return True