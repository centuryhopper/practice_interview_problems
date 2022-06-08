

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b1, b2 = 0, 0
        n, m = len(a), len(b)
        # a to decimal
        for i, c in enumerate(a):
            if c == '0':
                continue
            b1 += 2**(n-1-i)
        # b to decimal
        for i, c in enumerate(b):
            if c == '0':
                continue
            b2 += 2**(m-1-i)
        return bin(b1 + b2)[2:]
