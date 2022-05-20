class Solution:
    '''
    custom example
    [[1,0],[2,1],[3,1],[4,2],[4,3]]
    '''

    def canFinish(self, numCourses: int, preqs: List[List[int]]) -> bool:
        incoming = [0] * numCourses
        # adjacency list (set for faster look up)
        al = collections.defaultdict(list)
        for after, before in preqs:
            al[before].append(after)
            incoming[after]+=1
        # cnt the number of visited nodes
        cnt = 0
        # this queue should only contain nodes with no incoming edges provided that they either don't exist or have already been processed
        q = collections.deque()
        # any node with no incoming edges is ready to be visited
        for i in range(numCourses):
            if incoming[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            cnt+=1
            '''
            All vertices we can reach via an edge from the current vertex
            should have their incoming edge counts decremented.
            If one of these hits zero, add it to the queue,
            as it's ready to be included in our topological sort.
            '''
            for i in al[cur]:
                incoming[i]-=1
                if incoming[i] == 0:
                    q.append(i)
        # cycle detection
        if cnt != numCourses:
            return False
        return True






        return
