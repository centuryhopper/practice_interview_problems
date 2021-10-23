class Solution:
    # letters are in base 26
    def titleToNumber(self, ct: str) -> int:
        letterToNumber = lambda l: ord(l)-65+1
        ans = 0
        n = len(ct)
        for i,c in enumerate(ct):
            ans += letterToNumber(c) * 26**(n-1-i)
        return ans


