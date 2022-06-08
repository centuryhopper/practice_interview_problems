from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n < 2: return stones[0]
        h = []
        heapify(h)
        # push stones into maxheap
        for stone in stones:
            heappush(h, -stone)
        while len(h) > 1:
            y = -heappop(h)
            x = -heappop(h)
            if y - x > 0:
                heappush(h, -(y-x))
        return -h[0] if h else 0



