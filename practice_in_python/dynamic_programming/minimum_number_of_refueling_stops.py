
from heapq import heappush, heappop, heapify

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        #edge case
        if startFuel >= target:
            return 0
        h = []
        heapify(h)
        curPos = 0
        # refuel counts
        cnt = 0
        start = 0
        curFuel = startFuel
        # find a starting candidate
        while curFuel + curPos < target:
            # keep adding elements
            # until a station is unreachable
            # via current fuel amount
            # tmp is start + 1 so that if we don't go into the loop
            # we can have start be incremented by 1
            tmp = start + 1
            prevPos = curPos
            for i in range(start, len(stations)):
                fuelAtStation = stations[i][1]
                stationPos = stations[i][0]
                # if it's unreachable
                if stationPos - prevPos > curFuel:
                    tmp = i
                    break
                heappush(h, -fuelAtStation)
                curPos = stationPos
            start = tmp
            if not h: return -1
            # refueling
            curFuel = curFuel - (curPos - prevPos)
            val = -heappop(h)
            # print(val)
            curFuel += val
            cnt+=1

        return cnt








#region online cleaner solution


# class Solution:
#     def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
#         # priority queue
#         pq = []
#         res = i = 0
#         while startFuel < target:
#             while i < len(stations) and stations[i][0] <= startFuel:
#                 # Min heap to Max heap ("-")
#                 heapq.heappush(pq, -stations[i][1])
#                 i += 1
#             if not pq:
#                 return -1
#             startFuel += -heapq.heappop(pq)
#             res += 1
#         return res

#endregion