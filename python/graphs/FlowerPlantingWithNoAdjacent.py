import collections

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        al = collections.defaultdict(list)
        for x,y in paths:
            al[x].append(y)
            al[y].append(x)
        seen = set()
        colors = [0]*n
        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            
            # determine color for current garden
            for j in range(1,5):
                # make sure none of current garden's neighbors have
                # this color already before marking it
                shouldSkip = False
                for nei in al[i]:
                    if colors[nei-1] == j:
                        shouldSkip = True
                        break
                if shouldSkip: continue
                colors[i-1] = j
                break
                
            for nei in al[i]:
                dfs(nei)
        
        for i in range(n):
            dfs(i)
        return colors
    
