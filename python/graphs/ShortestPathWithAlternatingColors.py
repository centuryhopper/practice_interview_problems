class Solution:
    '''
    6
    r = [[0,1],[1,2],[3,4]]
    b = [[0,2],[0,3],[4,5],[2,5]]
    
5
[[0,1],[1,2],[2,3],[3,4]]
[[1,2],[2,3],[3,1]]
    
    
    '''
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        al = [{'r':[],'b':[]} for _ in range(n)]
        for x,y in redEdges:
            al[x]['r'].append(y)
        for x,y in blueEdges:
            al[x]['b'].append(y)
        # assume every node other than 0 is unreachable
        ans = [-1] * n
        ans[0] = 0
        seen = set([0])
        q = []
        # initialize level (breadth) at one because we're initializing all queue values with the neighbors of 0, regardless of the edge colors
        level = 1
        for node in al[0]['r']:
            q.append((node,'r'))
        for node in al[0]['b']:
            q.append((node,'b'))
        while q:
            # size is all the nodes to be processed the
            # current breadth value
            size = len(q)
            # process every node at the current breadth
            for _ in range(size):
                node, color = q.pop(0)
                if (node,color) in seen:
                    continue
                seen.add((node,color))
                # don't remark if already marked
                if ans[node] == -1:
                    ans[node] = level
                # if the current node is reached via a red edge then search all its
                # neighbors with outgoing blue edges, and vice versa
                oppositeColor = 'r' if color == 'b' else 'b'
                for nei in al[node][oppositeColor]:
                    q.append((nei,oppositeColor))
            # finished the current breadth,
            # so move on to the next
            level+=1
        
        return ans
                
                
            
        
