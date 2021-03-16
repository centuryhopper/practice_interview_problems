class Solution:

    def removePalindromeSub(self, s: str) -> int:

        def isPalin(s: str, i: int, j: int) -> bool:
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return isPalin(s, i+1, j-1)

        if 'a' not in s or 'b' not in s:
            return 0
        if isPalin(s, 0, len(s)-1):
            return 1

        return 2
