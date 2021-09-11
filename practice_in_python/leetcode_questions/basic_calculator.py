import re


class Solution:
    # skip spaces
    def calculate(self, s: str) -> int:
        ans = 0
        curVal = 0
        sign = 1
        lst = []
        # get rid of all spaces
        pieces = re.findall('\d{1,10}|\(|\)|[+-]', s)
        for piece in pieces:
            if piece.isdigit():
                curVal += int(piece) * sign
                ans += curVal
                curVal = 0
            elif piece == '+':
                sign = 1
            elif piece == '-':
                sign = -1
            elif piece == '(':
                # push current answer into stack for later use
                lst.append(ans)
                lst.append(sign)
                # reset for evaluating what is inside the parenthesis
                ans = 0
                sign = 1
            elif piece == ')':
                # evaluate current expression
                signVar = lst.pop()
                ans *= signVar
                cachedNum = lst.pop()
                ans += cachedNum
                sign = 1
                curVal = 0
        return ans
