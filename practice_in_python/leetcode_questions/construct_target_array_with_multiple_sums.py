from heapq import heappush, heappop, heapify

class Solution:
    '''implementation using maxheap'''
    def isPossible(self, target: List[int]) -> bool:
        h = []
        heapify(h)
        summ = 0

        for i, num in enumerate(target):
            # negative sign bc we're using a maxheap
            # maxheap is sorted by the tuple's first element
            heappush(h, (-num, i))
            summ+=num
        while -h[0][0] != 1:
            tup = heappop(h)
            maxVal, idx = -tup[0], tup[1]

            # print(target)
            remaining = summ - maxVal
            if remaining == 1 or maxVal == 1: break
            # avoid divide by 0 error from the if check below
            if remaining == 0: return False
            if maxVal <= remaining or maxVal % remaining == 0:
                # print(maxVal,remaining)
                return False

            # keep the summ up to date with the heap contents
            summ -= maxVal
            target[idx] %= remaining
            summ += target[idx]
            heappush(h, (-target[idx], idx))
            if target[idx] < 1:
                return False

        return True



# class Solution:
#     def isPossible(self, target: List[int]) -> bool:

#         maxVal = 0
#         while True:
#             maxVal = 0
#             idx = -1
#             summ = 0

#             # change to a max heap for better performance
#             for i,num in enumerate(target):
#                 if num > maxVal:
#                     maxVal = num
#                     idx = i
#                 summ += num

#             # print(target)
#             remaining = summ - maxVal
#             if remaining == 1 or maxVal == 1: break

#             # avoid divide by 0 error from the if check below
#             if remaining == 0: return False
#             if maxVal <= remaining or maxVal % remaining == 0:
#                 # print(maxVal,remaining)
#                 return False


#             target[idx] %= (summ - maxVal)
#             if target[idx] < 1:
#                 return False
#             # if maxVal == 1 or summ - maxVal == 1: break

#         return True



