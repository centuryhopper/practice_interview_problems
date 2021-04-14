from collections import deque


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        n = len(pushed)
        stack = deque()
        push = stack.append
        pop = stack.pop
        while i < n or j < n:
            if i < n:
                if pushed[i] != popped[j]:
                    if stack and stack[-1] == popped[j]:
                        pop()
                        j += 1
                    else:
                        push(pushed[i])
                        i += 1
                else:
                    i += 1
                    j += 1
            else:
                if stack and stack[-1] == popped[j]:
                    pop()
                    j += 1
                else:
                    return False
        return True


'''
more optimized solution found online:

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        num_popped = 0
        for n in pushed:
            st.append(n)
            while st and st[-1] == popped[num_popped]:
                st.pop()
                num_popped += 1
        return not st and num_popped == len(popped)

'''
