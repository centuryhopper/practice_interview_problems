from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # x is one end of the edge and y is the other
        # the intuition behind this algorithm is that if we can dfs from x to y without
        # going on the edge from x to y, then we have found a cycle
        # implemented using iterative DFS
        def hasCycle(adjLst,x,y) -> bool:
            nonlocal edges
            visited = set()
            lst = adjLst
            stack = [x]
            while stack:
                node = stack.pop()
                # if we come across y then we found a cycle
                if node == y:
                    # print(adjLst)
                    return True
                visited.add(node)
                neighbors = lst[node]
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    stack.append(neighbor)
            # print(adjLst)
            return False

        adjLst = defaultdict(list)
        for x,y in edges:
            if (hasCycle(adjLst,x,y)): return [x,y]
            adjLst[x].append(y)
            adjLst[y].append(x)

        return None