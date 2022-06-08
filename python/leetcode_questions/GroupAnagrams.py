from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(tuple(zip(sorted(Counter('dog').items()))) == tuple(zip(sorted(Counter('god').items()))))
        # d = defaultdict(list)
        # for s in strs:
        #     d[tuple(zip(sorted(Counter(s).items())))].append(s)
        # return d.values()
        
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return d.values()

#region more optimized solution online
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = {}
#         for i in strs:
#             temp = "".join(sorted(i))
#             if temp not in d:
#                 d[temp] = [i]
#             else:
#                 d[temp].append(i)
#         return d.values()
#endregion  