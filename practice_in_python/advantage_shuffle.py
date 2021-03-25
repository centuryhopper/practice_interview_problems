from collections import defaultdict, deque


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # store indices of original B array
        mapB = defaultdict(deque)
        for i, num in enumerate(B):
            mapB[num].append(i)
        A.sort()
        B.sort()
        # unused integers from sorted A
        unused = deque()
        # return array
        lst = [-1]*len(A)
        i, j = 0, 0
        # either both move ahead or only i moves
        # ahead, so j will never be greater than i
        while i < len(A):
            if A[i] > B[j]:
                lst[mapB[B[j]][0]] = A[i]
                mapB[B[j]].popleft()
                i += 1
                j += 1
            else:
                unused.append(A[i])
                i += 1
        if unused:
            for i,num in enumerate(lst):
                if num == -1:
                    lst[i] = unused[0]
                    unused.popleft()


        return lst






    
















# more optimized solution
# class Solution:
#     def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#       idx = list(range(len(B)))
#       idx.sort(key = lambda i: B[i])
#       A.sort()
#       res = [-1] * len(A)
#       start, end = 0, len(B) - 1
#       # iterate through sorted A and B
#       # if a can cover b, then correspond b with a
#       # if a cannot, correspond a with largest of b
#       for a in A:
#         if a > B[idx[start]]:
#           res[idx[start]] = a
#           start += 1
#         else:
#           res[idx[end]] = a
#           end -= 1
#       return res








# failed attempt
# class Solution:
#     def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#         # candidate indices
#         indices = []
#         # populate indices
#         for i, num in enumerate(A):
#             if num <= B[i]:
#                 indices.append(i)

#         for i in indices:
#             candidate = A[i]
#             antiCandidate = B[i]
#             # swapped = False
#             for v in range(len(A)):
#                 teammate = A[v]
#                 teammateOpponent = B[v]
#                 if v == i: continue
#                 # if swapped: break
#                 if candidate > teammateOpponent and teammate > antiCandidate:
#                     A[i], A[v] = A[v], A[i]
#                     # swapped = True



#         return A






