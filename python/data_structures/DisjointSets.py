

class DisjointSet:
    def __init__(self, n: int):
        # initially, all values will have a rank of 1
        self.rank = [1]*n
        # the values are 0 thru n-1, each with themselves as parents
        self.parent = list(range(n))

    # find the parent of i
    def find(self, i) -> int:
        parent = self.parent
        # the value is its own parent (base case)
        if parent[i] == i:
            return parent[i]
        # path compression via depth-first search
        # recursive call on its parent value until the value is its own parent
        parent[i] = self.find(parent[i])
        return parent[i]

    # if they have the same parent, do nothing.
    # otherwise, compare their ranks
    # the one with the lower rank will have the other as its new parent.
    # if they have the same rank, then either one can be the other's parent
    # but make sure that the one that becomes the parent gets its own rank + 1
    def union(self, x, y) -> None:
        parent, rank = self.parent, self.rank
        if parent[x] == parent[y]:
            print('x and y already have the same parent')
            return
        # check ranks
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[y] > rank[x]:
            parent[x] = y
        else:
            parent[x] = y
            # this would work too
            # parent[y] = x
            rank[y] += 1


if __name__ == '__main__':
    obj = DisjointSet(5)
    obj.union(0, 2)
    obj.union(4, 2)
    obj.union(3, 1)
    if obj.find(4) == obj.find(0):
        print('Yes')
    else:
        print('No')
    if obj.find(1) == obj.find(0):
        print('Yes')
    else:
        print('No')
