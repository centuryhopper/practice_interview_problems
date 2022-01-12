from heapq import heappush, heappop, heapify

class Solution:
    '''
    [[2,1,3],[3,3,7],[2,4,7],[1,5,7]]
    6

    [[2,1,5],[3,5,7]]
    3

    [[3,2,7],[3,7,9],[8,3,9]]
    11


    [[7,5,6],[6,7,8],[10,1,6]]
    16

    algorithm:
    -sort the trips array by the starting position
    -have an updated current capacity available
    -for each trip, look at from_i and drop all trips from the past that have ended
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip:trip[1])
        h = []
        heapify(h)
        cur = capacity

        for a,b,c in trips:
            if cur < 0:
                return False
            # keep removing passengers who have already reached their destination
            while h and b >= h[0][0]:
                cur+=heappop(h)[1]
            cur-=a
            heappush(h,(c,a))
            # print(cur)

        return cur >= 0