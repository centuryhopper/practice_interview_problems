from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # if len(s) == 1:
        #     if s.isalpha():
        #         return s
        #     return ''

        # traverse string forwards then backwards
        lst = deque(s)
        cnt = 0
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    lst[i] = ''
                else:
                    cnt -= 1
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                cnt += 1
            elif s[i] == '(':
                if cnt == 0:
                    lst[i] = ''
                else:
                    cnt -= 1
        return ''.join(lst)



# spaced optimized online solution
'''
from collections import namedtuple

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        bracket = namedtuple('bracket', 'paran index')
        stack = []


        for idx, char in enumerate(s):
            if char == '(':
                stack.append(bracket(char, idx))
            elif char == ')':
                if stack and stack[-1].paran == '(':
                    stack.pop()
                else:
                    stack.append(bracket(char, idx))

        stack = stack[::-1]
        valid_char = s
        print(stack)
        for bracket_to_remove in stack:
            valid_char = valid_char[:bracket_to_remove.index] + valid_char[bracket_to_remove.index + 1:]

        return valid_char
        
'''