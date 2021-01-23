from collections import defaultdict

class Solution:

    # approach:
    # store, sort, and restore => finished
    def diagonalSort(self, a: List[List[int]]) -> List[List[int]]:

        def inBounds(r, c) -> bool:
            return r < len(a) and c < len(a[0])

        m = len(a)
        n = len(a[0])

        d = defaultdict(list)

        # traverse each row
        for i in range(m-1, 0, -1):
            r, c = i,0
            while inBounds(r, c):
                d[r-c].append(a[r][c])
                r+=1
                c+=1
            d[r-c].sort(reverse=True)
            r,c = i,0
            while inBounds(r,c):
                a[r][c] = d[r-c].pop()
                r+=1
                c+=1
        # traverse each column
        for i in range(0, n):
            r, c = 0,i
            while inBounds(r, c):
                d[r-c].append(a[r][c])
                r += 1
                c += 1
            d[r-c].sort(reverse=True)
            r,c = 0,i
            while inBounds(r,c):
                a[r][c] = d[r-c].pop()
                r+=1
                c+=1
        return a

        

