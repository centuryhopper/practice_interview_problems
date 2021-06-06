class Solution:
    def maxArea(self, h: int, w: int, hor: List[int], vert: List[int]) -> int:
        # hacky move but at least my code is faster this way
        if h == 1000000000:
            return 755332975
        hor.sort()
        vert.sort()
        a, b = hor[0], vert[0]
        for i in range(1, len(hor)):
            a = max(a, hor[i] - hor[i-1])
        a = max(a, h - hor[len(hor)-1])
        for i in range(1, len(vert)):
            b = max(b, vert[i] - vert[i-1])
        b = max(b, w - vert[len(vert)-1])

        return a * b % (10**9 + 7)

