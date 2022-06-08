


class Solution:
    '''
3
[[1,2],[1,0],[2,0]]
[[1,0],[1,2]]

4
[[2,3],[2,1],[0,3],[0,1]]
[[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]

5
[[0,1],[1,2],[2,3],[3,4]]
[[0,4],[4,0],[1,3],[3,0]]



10
[[3,9],[3,2],[3,7],[9,5],[9,0],[9,6],[8,0],[8,1],[8,7],[5,0],[5,2],[5,1],[5,7],[5,6],[0,2],[0,1],[0,6],[2,1],[2,6],[4,1],[1,7],[1,6],[7,6]]


[[9,7],[7,3],[6,1],[1,8],[5,7],[3,8],[2,5],[7,9],[3,0],[4,8],[5,1],[5,3],[3,0],[9,8],[6,9],[5,0],[8,2],[3,6],[3,6],[1,0],[9,7],[9,5],[1,9],[0,4],[7,3],[9,8],[6,2],[7,9],[8,9],[0,5],[5,8],[9,8],[5,6],[7,6],[7,3],[2,1],[9,8],[8,2],[7,8],[9,8],[0,1],[8,9],[8,9],[6,1],[8,1],[8,6],[3,8],[8,9],[9,7],[8,7],[3,7],[9,7],[9,6],[4,2],[5,9],[3,0],[6,9],[7,8],[6,9],[2,1],[7,3],[0,5],[4,9],[5,6],[8,7],[9,7],[9,3],[1,0],[1,7],[7,9],[1,5]]

[true,false,false,false,true,false,false,false,true,false,true,false,true,false,false,true,true,true,true,false,true,true,false,false,false,false,false,false,false,false,false,false,true,true,false,true,false,true,false,false,true,false,false,false,true,true,false,false,true,true,true,true,true,true,false,true,false,false,false,true,false,false,false,true,true,true,false,false,true,false,false]

    '''
    def checkIfPrerequisite(self, n: int, prereqs: List[List[int]], queries: List[List[int]]) -> List[bool]:


        # I tried to use topo sort but failed
        '''
        if not prereqs: return [False]*n
        topo = []
        al = {i:[] for i in range(n)}

        # toposort algo
        incoming = [0] * n
        for x,y in prereqs:
            incoming[y]+=1
            al[x].append(y)
        # print(incoming)

        isReachable = [[False]*n for _ in range(n)]

        q = [i for i in range(n) if incoming[i] == 0]
        while q:
            cur = q.pop(0)
            topo.append(cur)
            for nei in al[cur]:
                incoming[nei]-=1
                isReachable[cur][nei] = True
                if incoming[nei] == 0:
                    q.append(nei)
                    # update for the final answers
                    for node in topo:
                        for nodeNei in al[node]:
                            if incoming[nodeNei] == 0:
                                isReachable[node][nei] = True


        # print(topo)
        # print(isReachable)
        # print(al)

        ans = []
        for x,y in queries:
            ans.append(isReachable[x][y])




        return ans
        '''
        '''
        floyd-warshall

        let v = num vertices in graph
        let dist = v * v array of minimum distances
        for each vertex v:
            dist[v][v] = 0
        for each edge(u,v):
            dist[u][v] = weight(u,v)
        for k from 1 to v:
            for i from 1 to v:
                for j from 1 to v:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        '''
        if not prereqs: return [False]*n

        dist = [[float('inf')]*n for _ in range(n)]
        for a,b in prereqs:
            dist[a][b] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        ans = [dist[a][b] != float('inf') for a,b in queries]

        return ans


















