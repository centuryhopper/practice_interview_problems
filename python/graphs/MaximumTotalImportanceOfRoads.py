from heapq import heappush,heappop,heapify

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance = [0]*n
        degrees = collections.defaultdict(list)
        for x,y in roads:
            # bi-directional
            degrees[x].append(y)
            degrees[y].append(x)
        h = []
        heapify(h)
        for i in range(n):
            heappush(h,(len(degrees[i]),i))
        cnt = 1
        for i in range(n):
            val = heappop(h)[1]
            # print(val)
            importance[val] = cnt
            cnt+=1
        # print(h)
        # print(importance)
        
        ans = 0
        seen = set()
        for i in range(1,n):
            for nei in degrees[i]:
                if (importance[nei], importance[i]) not in seen:
                    ans += importance[i] + importance[nei]
                    seen.add((importance[i], importance[nei]))
        
        return ans
        
        
        
        
