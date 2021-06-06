from heapq import heapify, heappush, heappop

# my first approach unoptimized
# O(n^2 + n log n) => O(n^2) runtime | O(n) space
# class Solution:
#     def maxPerformance(self, n: int, ss: List[int], es: List[int], k: int) -> int:
#         # (efficiency, speed)
#         lst = [(a,b) for a,b in zip(es, ss)]
#         # sort efficiency in decreasing order since it carries more weight than speed does
#         # according to the performance formula
#         lst.sort(reverse=True)
#         # print(lst)
#         # performance = sum(speeds of candidates) * min(respective efficiencies)
#         # maxheap
#         h = []
#         heapify(h)

#         best = 0
#         for i in range(n):
#             curSum = 0
#             # push all speed values left of i into heap
#             for j in range(i):
#                 heappush(h, -lst[j][1])
#             # print([abs(v) for v in h])
#             # pop k-1 elements out of heap
#             for _ in range(k-1):
#                 if h: curSum += (-heappop(h))
#                 else: break

#             curSum += lst[i][1]
#             # print(curSum, lst[i][1])
#             best = max(best, lst[i][0] * curSum)

#         return best % (7 + 10**9)


# my final optimized solution
# O(n log n) runtime | O(n) space
class Solution:
    def maxPerformance(self, n: int, ss: List[int], es: List[int], k: int) -> int:
        # (efficiency, speed)
        lst = list(zip(es, ss))
        # sort efficiency in decreasing order since it carries more weight than speed does
        # according to the performance formula
        lst.sort(reverse=True)
        # print(lst)
        # performance = sum(speeds of candidates) * min(respective efficiencies)
        # minheap
        h = []
        heapify(h)

        best = 0
        curSum = 0
        for eff, speed in lst:
            heappush(h, speed)
            curSum += speed
            # kick out the smallest one
            if len(h) > k:
                curSum -= heappop(h)
            best = max(best, eff * curSum)

        return best % (7 + 10**9)


# found a pretty darn optimized solution online
# class Solution:
#     def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
#         speeds = 0
#         speedHeap = []
#         tr = 0
#         indexes = list(range(n))
#         indexes.sort(key=lambda i: -efficiency[i])

#         speedCount = 0
#         for i in indexes:
#             heappush(speedHeap, speed[i])
#             speeds += speed[i]
#             speedCount += 1
#             if speedCount > k:
#                 lowSpeed = heappop(speedHeap)
#                 speeds -= lowSpeed
#             tr = max(tr, speeds * efficiency[i])

#         return tr % 1000000007
