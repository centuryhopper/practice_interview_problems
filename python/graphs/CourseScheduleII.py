class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = {i:set() for i in range(numCourses)}
        for c, p in prerequisites:
            incoming[c].add(p)
        ans = []
        # queue should only contain nodes with no incoming edges at any time.
        # initialize all nodes with no incoming edges to q
        q = collections.deque([k for k,v in incoming.items() if not v])

        while q:
            cur = q.popleft()
            incoming.pop(cur)
            ans.append(cur)
            for k, v in incoming.items():
                if cur in v:
                    if len(v) == 1:
                        q.append(k)
                    v.remove(cur)

        # detect cycles
        if len(ans) != numCourses:
            return []

        return ans








