import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl = len(s)
        pl = len(p)
        if sl < pl: return []
        pc = collections.Counter(p)
        curCnt = collections.Counter(s[0:pl])
        ans = []
        for i in range(sl-pl+1):
            # don't increment on the first iteration because the
            # counter is already initialized with the correct info
            if i > 0:
                curCnt[s[i+pl-1]]+=1
            if curCnt == pc:
                ans.append(i)
            curCnt[s[i]]-=1

        return ans

