from itertools import chain

class Solution:
    # O(n log n) one-liner
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted(chain(*matrix))[k-1]


# Heap, n log k
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
# 		return heapq.nsmallest(k, [x for row in matrix for x in row])[-1]


