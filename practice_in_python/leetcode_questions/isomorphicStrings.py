# from itertools import chain
from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = defaultdict(list), defaultdict(list)
        for i in range(len(s)):
            ds[s[i]].append(i)
            dt[t[i]].append(i)

        return all(l1 == l2 for l1, l2 in zip(ds.values(), dt.values()))
