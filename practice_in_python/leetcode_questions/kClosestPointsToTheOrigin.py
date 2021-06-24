from heapq import heappush, heappop, heapify

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapify(h)

        for p in points:
            eucl = (p[0]**2) + (p[1]**2)
            heappush(h, (-eucl,p))
            if len(h) > k:
                heappop(h)
        ret = []
        while h:
            ret.append(heappop(h)[1])

        return ret