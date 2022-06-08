from typing import List

class Solution:

    '''
    [[1,1,0],
     [1,1,0],
     [0,0,1]]


[[1,0,0,1],
 [0,1,1,0],
 [0,1,1,1],
 [1,0,1,1]]
    '''
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        record = [-1]*n
        # all nodes reached since the starting node will all share the same mark
        mark = 0
        def dfs(cur):
            # if this node has been visited before
            if record[cur] != -1:
                return
            record[cur] = mark
            for j in range(n):
                if i != j and isConnected[cur][j] == 1:
                    dfs(j)


        # dfs from every node to find provinces
        for i in range(n):
            dfs(i)
            # change the mark for the next set of provinces
            mark+=1

        # return the count of the number of unique groups
        return len(dict.fromkeys(record))










