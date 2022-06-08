class Solution:
    '''
    97 - 122 => a-z
    65 - 90 => A-Z
    97 - 65 = 32
    122 - 90 = 32
    '''
    # avoids using s.lower() because only cheaters use that for this problem :P
    def toLowerCase(self, s: str) -> str:
        ret = ''
        for c in s:
            if not c.isalpha() or 97 <= ord(c) <= 122:
                ret += c
            else:
                ret += chr(ord(c) + 32)
        return ret




