class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # only possible if there are at least n - 1 connections
        if len(connections) < n - 1: return -1
        
        # use union-find algorithm to find the number of all unique groups and the answer will be
        # that number - 1
        parent = list(range(n))
        rank = [1]*n
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            xr = find(x)
            yr = find(y)
            if xr == yr:
                return
            if rank[xr] > rank[yr]:
                parent[yr] = xr
            elif rank[yr] > rank[xr]:
                parent[xr] = yr
            else:
                parent[xr] = yr
                rank[yr]+=1
                          
        # build adjacency list
        al = {i:[] for i in range(n)}
        seen = set()
        for x,y in connections:
            al[x].append(y)
            al[y].append(x)
        
        def dfs(parent, child):
            if child in seen:
                return
            union(parent,child)
            seen.add(child)
            for nei in al[child]:
                dfs(parent,nei)
        # find all unique groups
        # doing a dfs from every node
        for i in range(n):
            dfs(i,i)
            
        return len(set(parent)) - 1
        
        
        
        
        
        
        
            
            
            
