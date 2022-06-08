class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        return self.hammingWeight(n//2) + (1 if n & 1 else 0)
