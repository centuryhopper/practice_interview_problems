class Solution:
    '''
    
[[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]

[[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]]
    '''
    
    
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        # stones.sort(key=lambda x:x[0])
        parent = list(range(n))
        rank = [1]*n
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            xr = find(x)
            yr = find(y)
            if xr == yr: return
            if rank[xr] > rank[yr]:
                parent[yr] = xr
            elif rank[xr] < rank[yr]:
                parent[xr] = yr
            else:
                parent[xr] = yr
                rank[yr]+=1
        
        # iterating twice makes it work since the first time
        # might change some values not as desired
        # second time we the algorithm will avoid unioning values if
        # they're already in the same group
        for _ in range(2):
            for i in range(n):
                ir,ic = stones[i]
                for j in range(i+1,n):
                    jr,jc = stones[j]
                    if ir == jr or ic == jc:
                        union(i,j)
                        # print(f'after unioning i:{i}, j:{j}')
                        # print(parent, (ir,ic), (jr,jc))
                        # print(rank)
                        # print()
        c = collections.Counter(parent)
        # print(c)
        
        ans = 0
        for _,v in c.items():
            ans += v-1
        
        return ans
        
        
