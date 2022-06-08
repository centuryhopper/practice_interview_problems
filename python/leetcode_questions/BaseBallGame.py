from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op.isdigit() or op[0] == '-':
                stack.append(int(op))
            elif op == '+':
                stack.append(stack[-2] + stack[-1])
            elif op =='C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1]*2)
        return sum(stack)



