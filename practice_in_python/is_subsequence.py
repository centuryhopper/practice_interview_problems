

class Solution:

    # recursive
    def helper(self, s: str, si: int, t: str, ti: int) -> bool:
        if si >= len(s):
            return True
        if ti >= len(t):
            return False

        if s[si] == t[ti]:
            return self.helper(s, si+1, t, ti+1)
        return self.helper(s, si, t, ti + 1)


    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False

        return self.helper(s,0,t,0)



        