from typing import List

class DisJointSet:
    def __init__(self, n):
        '''
        initially create as many disjoint sets as the number of points, n
        '''
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        '''
        find the representative point's set that the argument "point" belongs to
        '''
        parent = self.parent
        if parent[p] == p:
            return p
        parent[p] = self.find(parent[p])
        return parent[p]

    def union(self,p1,p2):
        '''
        combine p1 and p2 into one set is they're not in the same set already
        '''
        parent = self.parent
        rank = self.rank
        p1Root, p2Root = self.find(p1), self.find(p2)
        if p1Root == p2Root:
            return
        if rank[p1Root] > rank[p2Root]:
            parent[p2Root] = p1Root
        elif rank[p1Root] < rank[p2Root]:
            parent[p1Root] = p2Root
        else:
            parent[p1Root] = p2Root
            rank[p2Root] += 1


# this problem was implemented using kruskal's algorithm

class Solution:
    '''
    [[0,0],[2,2],[3,10],[5,2],[7,0]]

    '''
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        getManhattanDist = lambda p1,p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        # get all edges of graph (edges are formed from manhattan distances)
        edges = [(i, j, getManhattanDist(points[i],points[j])) for i in range(n) for j in range(i+1,n)]
        # print([(points[i],points[j]) for i in range(n) for j in range(i+1,n)])
        # sort in non decreasing order
        edges.sort(key=lambda t:t[2])

        # print(edges)
        ds = DisJointSet(n)
        ans = 0
        for edge in edges:
            i,j,dist = edge
            # if the points are already in the same set, then we shouldn't union them again to avoid cycles
            if ds.find(i) == ds.find(j):
                continue
            ds.union(i,j)
            ans += dist

        return ans










