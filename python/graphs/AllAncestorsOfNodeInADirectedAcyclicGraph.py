import collections
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # plan: reverse the edges and then bfs once at every node
        al = {i:[] for i in range(n)}
        # reversed graph adjacency list
        for x,y in edges:
            al[y].append(x)
        
        def bfs(startNode):
            q = collections.deque([startNode])
            seen = set()
            ans = []
            while q:
                node = q.pop()
                for nei in al[node]:
                    if nei in seen:
                        continue
                    seen.add(nei)
                    ans.append(nei)
                    q.append(nei)
            return sorted(ans)
        
        return [bfs(i) for i in range(n)]
                
            
            
        
        
