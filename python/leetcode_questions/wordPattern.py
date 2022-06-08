class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        # print(s)
        if len(s) != len(pattern):
            return False
        d = {}
        # check one way
        for i in range(len(s)):
            if pattern[i] in d:
                if d[pattern[i]] != s[i]:
                    return False
            d[pattern[i]] = s[i]
        # clear the dictionary to check the other way
        d.clear()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != pattern[i]:
                    return False
            d[s[i]] = pattern[i]
        return True
