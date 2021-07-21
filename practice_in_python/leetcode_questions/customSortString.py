from heapq import heappush, heappop, heapify


#region my solution

class Solution:
    # time: O(len(s))
    # space: O(26) => O(1)
    def customSortString(self, order: str, s: str) -> str:
        d = {c:i for i,c in enumerate(order)}
        lst = []
        h = []
        heapify(h)
        for c in s:
            if c not in d:
                lst.append(c)
            else:
                heappush(h, (d[c], c))
        while h:
            lst.append(heappop(h)[1])
        return ''.join(lst)
        
        
        
        
#endregion