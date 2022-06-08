from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # we don't need a visited set because we assume the input graph is directed and acyclic
        n = len(graph)
        source = 0
        target = n-1
        ans = []
        def dfs(cur, graph, path):
            nonlocal ans
            if cur == target:
                ans.append(path)
                return
            # nn means neighbor node
            for nn in graph[cur]:
                dfs(nn,graph,path+[nn])
        dfs(source,graph,[source])
        return ans
