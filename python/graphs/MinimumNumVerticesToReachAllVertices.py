class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # the goal is to count the number of vertices with no incoming edges
        # initially we can assume all nodes have incoming edges unless proven otherwise
        ans = set(range(n))
        for _, to in edges:
            if to in ans:
                ans.discard(to)
        return ans
                
        
        
