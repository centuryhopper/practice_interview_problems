class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        res = None
        stack = []
        for token in tokens:
            # print(stack, res, token)
            # include digits and negative numbers
            if token.isdigit() or (token[0] == '-' and len(token) > 1):
                stack.append(token)
            else:
                r = int(stack.pop())
                l = int(stack.pop())
                if token == '+':
                    res = l + r
                elif token == '-':
                    res = l - r
                elif token == '*':
                    res = l * r
                elif token == '/':
                    # division can be handled like so rather than what I previously did
                    # in the commented out code below
                    res = int(l/r)

                stack.append(res)

        return res


# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         if len(tokens) == 1:
#             return int(tokens[0])
#         res = None
#         stack = []
#         for token in tokens:
#             # print(stack, res, token)
#             # include digits and negative numbers
#             if token.isdigit() or (token[0] == '-' and len(token) > 1):
#                 stack.append(token)
#             else:
#                 r = int(stack.pop())
#                 l = int(stack.pop())
#                 if token == '+':
#                     res = l + r
#                 elif token == '-':
#                     res = l - r
#                 elif token == '*':
#                     res = l * r
#                 elif token == '/':
#                     if (l >= 0 and r >= 0) or (l < 0 and r < 0):
#                         res = l // r
#                     elif l < 0:
#                         l *= -1
#                         res = l // r
#                         res *= -1
#                     elif r < 0:
#                         r *= -1
#                         res = l // r
#                         res *= -1

#                 stack.append(res)

#         return res
