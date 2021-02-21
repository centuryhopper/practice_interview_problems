
class Solution:

    # approach: reverse string and traverse
    # if the next character is bigger, we add, otherwise we subtract
    def romanToInt(self, s: str) -> int:
        d =\
            {
                'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500,
                'M': 1000,
            }
        s = s[::-1]
        retSum = d[s[0]]
        for i in range(1, len(s)):
            retSum = retSum + d[s[i]] \
                if d[s[i]] >= d[s[i-1]] else retSum - d[s[i]]

        return retSum


'''

more optimized solution

class Solution:

    # approach: traverse backwards using a map
    # if the previous character is bigger, we add, otherwise we subtract
    def romanToInt(self, s: str) -> int:
        d =\
        {
            'I':1,'V':5,'X':10,
            'L':50,'C':100,'D':500,
            'M':1000,
        }
        retSum = d[s[-1]]
        for i in range(len(s)-2, -1, -1):
            retSum = retSum + d[s[i]] if d[s[i]] >= d[s[i+1]] else retSum - d[s[i]]
        return retSum




'''


'''
Failed attempt:
class Solution:

    # approach: traverse backwards using a map
    # if the next character is bigger, we add, otherwise we subtract
    def romanToInt(self, s: str) -> int:
        d =\
        {
            'I':1,'V':5,'X':10,
            'L':50,'C':100,'D':500,
            'M':1000,
        }
        if len(s) == 1:
            return d[s[0]]

        retSum = 0
        # always caches the most recent even indexed character
        prev = ''
        for i, c in enumerate(reversed(s)):
            if i & 1:
                retSum = retSum - d[c] if d[c] < d[prev] else retSum + d[c]
            else:
                prev = c
                retSum += d[c]
        return retSum

'''
