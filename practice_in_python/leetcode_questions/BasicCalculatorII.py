class Solution:
    '''
    The idea is to handle multiplication and division operators within the loop iterations because they have higher precedence than their addition and subtraction counterparts. We treat subtraction signs as pushing the number to the right of it as a negative number (since a - b is the same as a + (-b)). Doing so, we can solve the problem in one pass O(n) time, where n is the length of the string
    '''
    def calculate(self, s: str) -> int:
        stack = []
        ops = set('+/-*')
        cur = 0
        lastSeenOp = '+'
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in ops:
                if lastSeenOp == '+':
                    stack.append(cur)
                elif lastSeenOp == '-':
                    stack.append(-cur)
                elif lastSeenOp == '*':
                    stack[-1]*=cur
                elif lastSeenOp == '/':
                    stack[-1] = int(stack[-1]/cur)
                lastSeenOp = c
                cur = 0
        if lastSeenOp == '+':
            stack.append(cur)
        elif lastSeenOp == '-':
            stack.append(-cur)
        elif lastSeenOp == '*':
            stack[-1]*=cur
        elif lastSeenOp == '/':
            stack[-1] = int(stack[-1]/cur)

        return sum(stack)






