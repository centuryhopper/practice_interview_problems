from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        #size of the heap
        size = 0

        for num in nums:
            heappush(heap, num)
            size += 1
            if size > k:
                heappop(heap)
                size -= 1



        # print(heap)

        return heap[0]