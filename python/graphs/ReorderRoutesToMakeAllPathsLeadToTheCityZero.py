class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        Treat the graph as undirected. Start a bfs from the root, if you come across an edge in the forward direction, you need to reverse the edge.
        '''
        al = {i:[] for i in range(n)}
        # f for forward, r for need to reverse
        for x,y in connections:
            al[x].append((y,'r'))
            al[y].append((x,'f'))
        q = [(0,'f')]
        seen = set()
        # count the number of edges that need to be reversed
        cnt = 0
        while q:
            cur, status = q.pop(0)
            if cur in seen:
                continue
            seen.add(cur)
            cnt = cnt if status == 'f' else cnt + 1
            for nei in al[cur]:
                q.append(nei)
        
        return cnt
                
            
            
        
            
        
        
