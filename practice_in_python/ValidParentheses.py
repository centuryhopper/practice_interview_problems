from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False

        # char array
        # lst = list(s)
        # print(lst)

        # simulate a stack with deque
        d = deque()

        for c in s:

            if c == '}':
                if len(d) > 0 and d[-1] == '{':
                    d.pop()
                else:
                    return False

            elif c == ')':
                if len(d) > 0 and d[-1] == '(':
                    d.pop()
                else:
                    return False

            elif c == ']':
                if len(d) > 0 and d[-1] == '[':
                    d.pop()
                else:
                    return False
            else:
                d.append(c)

        return len(d) == 0
            


# clever online sample solution by someone else
# class Solution:
#     def isValid(self, s: str) -> bool:
#         ob = []
#         brackets = {'(':')', '{':'}', '[':']'}
#         for bracket in s:
#             if bracket in brackets:
#                 ob.append(bracket)
#                 continue
#             if not ob:
#                 return False
#             b = ob.pop()
#             if bracket != brackets[b]:
#                 return False
#         return not ob