
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack will hold a bunch of lists with only two items
        # i.e. character and counter of that character
        stack = []
        for c in s:
            if stack:
                if c == stack[-1][0] and stack[-1][1] == k-1:
                    stack.pop()
                elif c == stack[-1][0]:
                    # update counter
                    stack[-1][1]+=1
                else:
                    print(c, end=' ')
                    stack.append([c,1])
            else:
                stack.append([c,1])
        # print()
        # print(stack)

        return ''.join([elem[0]*elem[1] for elem in stack])



























# online optimized solution
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         remove = []
#         ## Generating possible duplicates
#         for ch in set(s):
#             remove.append(ch*k)

#         old,new = s,s
#         while True:
#             for candidate in remove:
#                 new = new.replace(candidate,"")
#             if len(old) == len(new):
#                 break
#             old = new
#         return old
