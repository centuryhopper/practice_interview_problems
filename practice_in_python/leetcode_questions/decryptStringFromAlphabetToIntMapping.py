class Solution:
    def freqAlphabets(self, s: str) -> str:
        lst = []
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i+2] == '#':
                lst.append(chr(97+int(s[i:i+2])-1))
                i += 3
            else:
                lst.append(chr(97+int(s[i])-1))
                i += 1

        return ''.join(lst)
