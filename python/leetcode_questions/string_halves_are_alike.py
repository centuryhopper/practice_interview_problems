

class Solution:
    def __init__(self):
        self.st = {'a','e','i','o','u'}
    def is_vowel(self, c:str) -> bool:
        return c in st
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        # divider
        lb = ((l - 1) // 2) + 1
        cnt1,cnt2 = 0,0
        for i in range(lb):
            if s[i].lower() in self.st:
                cnt1 += 1
        for i in range(lb, l):
            if s[i].lower() in self.st:
                cnt2 += 1
        return cnt1 == cnt2






# more optimized solution
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         if not s or len(s) == 1:
#             return False
#         l = len(s)
#         t = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
#         mid = l // 2
#         cnt1 = sum((1 for e in s[:mid] if e in t))
#         cnt2 = sum((1 for e in s[mid:] if e in t))
#         return cnt1 == cnt2