class Solution:
    '''
    Try every pair of different cities and calculate its network rank.
    The network rank of two vertices is almost the sum of their degrees.
    How can you efficiently check if there is a road connecting two different cities?
    '''

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        '''
        0: {1,3}
        1: {0,2,3}
        2: {1}
        3: {0,1}
        '''
        al = {i:set() for i in range(n)}
        for x,y in roads:
            al[x].add(y)
            al[y].add(x)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                # sum up the degrees of nodes i and j
                # and only count the edge connecting nodes i and j once
                ans = max(ans,len(al[i]) + len(al[j]) - (1 if j in al[i] else 0))
            
        return ans
        
        
