from heapq import heappush,heappop,heappush

#region not so optimized solution
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        cur,cnt = 0,0
        h = []
        heapify(h)
        for num in arr:
            if num == cur:
                cnt+=1
            else:
                if cur != 0:
                    # we've tracked at least
                    # one type of value in
                    # the array
                    heappush(h, (-cnt, cur))
                cur = num
                cnt = 1
        if len(h) != len(set(arr)):
            heappush(h, (-cnt, cur))
        
        # print(h)
        threshold = len(arr) // 2
        cnt = 0
        ret = 0
        while cnt < threshold:
            ret+=1
            cnt+=-heappop(h)[0]
        return ret

#endregion

