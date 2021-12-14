from collections import Counter

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        rLen, mLen = len(r), len(m)
        if mLen < rLen:
            return False
        rc = Counter(r)
        mc = Counter(m)
        return all(rc[c] <= mc[c] for c in r)
