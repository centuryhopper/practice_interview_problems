class Solution:
    '''
    ["a!=b","c==c","b==d","x!=z"]
    '''
    def equationsPossible(self, equations: List[str]) -> bool:
        # print(equations)
        # check all equalities first
        # equations.sort(key=lambda x:x[1],reverse=True)
        # print(equations)
        parent = list(range(26))
        rank = [1] * 26
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            xr = find(x)
            yr = find(y)
            if xr == yr:
                # print(xr,yr)
                return False
            if rank[xr] > rank[yr]:
                parent[yr] = xr
            elif rank[xr] < rank[yr]:
                parent[xr] = yr
            else:
                parent[xr] = yr
                rank[yr]+=1
            return True
        # if didnt sort then we would loop twice
        for _ in range(2):
            for e in equations:
                if e[1] == '=':
                    union(ord(e[0])-97,ord(e[3])-97)
                else:
                    # if already in the same set
                    # print(ord(e[0])-97,ord(e[3])-97)
                    if find(ord(e[0])-97) == find(ord(e[3])-97):
                        return False
        return True
                
        
        
        
