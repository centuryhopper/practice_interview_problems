import bisect
from math import sqrt



class Solution:
    def numFactoredBinaryTrees(self, lst: List[int]) -> int:
        def rec_help(lst, i,j,k) -> int:


            if i < 0 and j < 0: return rec_helper(lst, k-2,k-2)

            # end of recursion
            if j < 0: return 0

            # didn't find factors for k
            if i < 0:
                return rec_help(lst, j-1, j-1, k)
            if lst[i]*lst[j] == lst[k]:
                if i == j:
                    return 1 + rec_help(lst, i-1, i-1, k-1)
                else:
                    return 2 + rec_help(lst, i, i, k-1)
            # scan with another i but keep the same j and k
            return 1 + rec_help(lst, i-1, j, k)

        lst.sort()
        # n = len(lst)
        # return rec_help(lst, n-2,n-2, n-1)

        # each key will represent a root node with key in it
        # and the corresponding value will represent the total possible number
        # of possible binary trees
        d = {}

        # overall counter
        retVal = 0
        for i in range(len(lst)):
            currentCount = 1
            for j in range(i):

                # lst[j] is a potential factor of lst[i]
                # and if so, we also need to check to see
                # if we've seen its complement already in our map
                if lst[i] % lst[j] == 0 and lst[i] / lst[j] in d:

                    # add the values of j and i/j to our current value
                    currentCount += (d[lst[j]] * d[lst[i] / lst[j]])
            d[lst[i]] = currentCount
            retVal += currentCount

        return retVal % (7+10**9)


        









# class Solution:
#     def numFactoredBinaryTrees(self, arr: List[int]) -> int:
#         mod = 1000000007
#         arr = sorted(set(arr))
#         table = {num: 1 for num in arr}

#         for num in arr[1:]:
#             for d in arr[:bisect.bisect(arr, int(sqrt(num)))]:
#                 if num / d in table:
#                     table[num] += table[d] * table[num / d] if d == num / \
#                         d else table[d] * table[num / d] * 2
#             table[num] %= mod

#         return sum(table.values()) % mod
