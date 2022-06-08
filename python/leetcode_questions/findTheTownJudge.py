from collections import defaultdict


#region most space optimized solution I can come up with
from collections import defaultdict

class Solution:
    '''
    Have a dict[int, int], d,
    For each x such that 1 <= x <= n, x is a town judge
    if and only if d[x] == n - 1 and x doesn't trust anyone else
    '''
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1: return 1
        # key is the number, value will be the count of all numbers that trust the key
        d = defaultdict(int)
        # the ith bit toggled off means trust no one, and toggled on means trusts at least one other number
        stateChecker = 0
        # a trusts b
        for a,b in trust:
            d[b]+=1
            stateChecker |= (1 << a)
        # print(bin(stateChecker))
        for k,v in d.items():
            if v == n - 1 and stateChecker & (1 << k) == 0:
                return k
        return -1

#endregion


#region more optimized solution
# class Solution:
#     '''
#     Have a dict[int, set[int]], d
#     For each x such that 1 <= x <= n, x is a town judge
#     if and only if d[x]'s size == n - 1 and x is not in any of the other n - 1 sets.
#     '''
#     def findJudge(self, n: int, trust: list[list[int]]) -> int:
#         # # returns true if x exists
#         # # at least one of the sets in d.values()
#         # def trustsAtLeastOne(x, d) -> bool:
#         #     return any((x in st for st in d.values()))
        
#         if n == 1: return 1
            
#         # key is the number, value is the set of all other numbers that trust the key
#         d = defaultdict(set)
        
#         # the ith bit toggled off means trust no one, and toggled on means trusts at least one other number
#         stateChecker = 0
#         # a trusts b
#         for a,b in trust:
#             d[b].add(a)
#             stateChecker |= (1 << a)
#         # print(bin(stateChecker))
#         for k,v in d.items():
#             # everyone trusts the town judge and the town judge trusts no one
#             # if len(v) == n - 1 and not trustsAtLeastOne(k,d):
#             #     return k
#             if len(v) == n - 1 and stateChecker & (1 << k) == 0:
#                 return k
#         return -1
#endregion


#region unoptimized solution

# class Solution:
#     '''
#     Have a dict[int, set[int]], d
#     For each x such that 1 <= x <= n, x is a town judge
#     if and only if d[x]'s size == n - 1 and x is not in any of the other n - 1 sets.
#     '''
#     def findJudge(self, n: int, trust: list[list[int]]) -> int:
#         # returns true if x exists
#         # at least one of the sets in d.values()
#         def trustsAtLeastOne(x, d) -> bool:
#             return any((x in st for st in d.values()))
        
#         if n == 1: return 1
            
#         # key is the number, value is the set of all other numbers that trust the key
#         d = defaultdict(set)
#         # a trusts b
#         for a,b in trust:
#             d[b].add(a)
#         # print(d)
#         for k,v in d.items():
#             # everyone trusts the town judge and the town judge trusts no one
#             if len(v) == n - 1 and not trustsAtLeastOne(k,d):
#                 return k
        
#         return -1
#endregion