from sortedcontainers import SortedList
from typing import List


class Solution:

    '''
    [[1,3],[2],[3],[]]

    [[3],[2],[1],[]]
    '''

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        my TLE solution
        ret = SortedList()
        def dfs(start,cur,visited):
            if cur in visited:
                return False
            if not graph[cur]:
                return True
            visited.add(cur)
            ans = True
            for neighbor in graph[cur]:
                ans &= dfs(start, neighbor, visited)
            # backtrack handling
            visited.remove(cur)
            return ans

        for i in range(len(graph)):
            ans = dfs(i,i,set())
            # print(i, ans)
            if ans:
                ret.add(i)
        return ret
        '''


        # working solution. Credits to NeetCode https://www.youtube.com/watch?v=Re_v0j0CRsg
        safe = {}
        ans = []

        def dfs(cur):
            if cur in safe:
                return safe[cur]
            # assume it is false initially
            safe[cur] = False
            for neighbor in graph[cur]:
                # if at least one neighbor returns false
                # then we know we're not a safe node
                if not dfs(neighbor):
                    return False

            # processed every neighbor at this point,
            # we now can confirm the current node is safe
            safe[cur] = True
            return True
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)




        return ans

