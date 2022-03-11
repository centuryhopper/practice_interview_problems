class Solution:
    '''
    "100[leetcode]"

    '''
    def decodeString(self, s: str) -> str:
        def getClosingBracketIndex(s,i,o,c):
            '''string s'''
            # return the index when a match has been found
            if o != 0 and c != 0 and o == c:
                return i-1
            if s[i] == '[':
                return getClosingBracketIndex(s,i+1,o+1,c)
            if s[i] == ']':
                return getClosingBracketIndex(s,i+1,o,c+1)
            return getClosingBracketIndex(s,i+1,o,c)
        def rec(s):
            if not s:
                return ''
            i,c = 0, ''
            #region get the number if it exists
            while i < len(s) and s[i].isdigit():
                c+=s[i]
                i+=1
            #endregion
            if c and c.isdigit():
                # get start and end bracket indices
                st = i
                e = getClosingBracketIndex(s,0,0,0)
                return int(c) * rec(s[st+1:e]) + rec(s[e+1:])

            return s[0] + rec(s[i+1:])
        return rec(s)

