import collections
from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        al = collections.defaultdict(list)
        for x,y in pairs:
            al[x].append(y)
            al[y].append(x)
        def dfs(al,idx,indices,chars,visited):
            if idx in visited:
                return
            visited.add(idx)
            indices.append(idx)
            chars.append(s[idx])
            for neighbor in al[idx]:
                dfs(al,neighbor,indices,chars,visited)


        visited = set()
        ans = ['']*len(s)
        for i,c in enumerate(s):
            # make sure we didn't dfs this index already
            if i not in visited:
                indices, chars = [],[]
                dfs(al,i,indices,chars,visited)
                indices.sort()
                chars.sort()
                for i in range(len(chars)):
                    ans[indices[i]] = chars[i]

        return ''.join(ans)



