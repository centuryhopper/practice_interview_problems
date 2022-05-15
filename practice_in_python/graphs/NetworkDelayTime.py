# from sortedcontainers import SortedList
from heapq import heappush, heappop, heapify
from collections import defaultdict
from typing import List

class Solution:
    '''
    [[2,1,1],[2,3,5],[3,4,1],[3,5,6],[4,5,2]]
    5
    2

[[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
5
1

    '''
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        al = defaultdict(list)
        for u,v,w in times:
            al[u].append((v,w))
        ans = 0
        seen = set()
        # start with the source node
        h = [(0,k)]
        heapify(h)
        while h:
            curDist, curNode = heappop(h)
            # don't process this node again if we've already done so
            if curNode in seen:
                continue
            seen.add(curNode)
            ans = max(ans,curDist)

            for v,w in al[curNode]:
                if v not in seen:
                    # add the current node weight relative to the source (curDist) to the cost of reaching the neighbor (w)
                    heappush(h, (curDist+w,v))

        # only return the answer if all nodes have been visited
        return ans if len(seen) == n else -1





















