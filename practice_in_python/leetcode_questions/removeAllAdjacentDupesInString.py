
# my solution (Runtime: 60 ms)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = ['$']
        for c in s:
            if c == l[-1]:
                l.pop()
            else:
                l.append(c)
        return ''.join(l[1:])


#region interesting online solution (40 ms)
'''
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        duplicates = [2*ch for ch in ascii_lowercase]
        prev_length = -1
        while prev_length!=len(s):
            prev_length=len(s)
            for d in duplicates:
                s=s.replace(d, '')
        return s
'''
#endregion