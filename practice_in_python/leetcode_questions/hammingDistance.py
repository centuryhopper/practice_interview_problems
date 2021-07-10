

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cur = 0
        # ints on a typical machine have 32 bits
        for i in range(32):
            xIth = 1 if x & (1 << i) else 0
            yIth = 1 if y & (1 << i) else 0
            # print(xIth,yIth)
            cur += (xIth ^ yIth)
        return cur
