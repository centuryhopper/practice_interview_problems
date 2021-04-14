from heapq import heappush, heappop, heapify

class Solution:
    def findLongestWord(self, s: str, ws: List[str]) -> str:

        # checks whether w is a subsequence of s,
        # where len(w) <= len(s)
        def is_subseq(w: str, s: str) -> bool:
            it = iter(s)
            return all(c in it for c in w)


        validMax = 0
        minheap = [""]
        heapify(minheap)
        for w in ws:
            if is_subseq(w, s):
                if validMax <= len(w):
                    validMax = len(w)
                    heappush(minheap, w)

        # pop off all strings that aren't as long as
        # the validMax, so that we either return a valid string in the min
        while minheap:
            if len(minheap[0]) < validMax:
                heappop(minheap)
            else:
                break
        return minheap[0]
