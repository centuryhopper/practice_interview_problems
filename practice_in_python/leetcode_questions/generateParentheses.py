import functools

#region my final solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        #region backtracking algorithm
        def rec(n,sLst,opening,closing) -> None:
            nonlocal lst
            # cant continue off this state
            # since the parentheses with inbalanced count
            # as such is impossible to fix
            if closing > opening:
                return
            # opening parenthesis have a max value of n in order to be balanced
            if opening > n:
                return
            # balanced parenthesis case
            if opening == closing == n:
                lst.append(''.join(sLst))
                return
            sLst.append('(')
            rec(n,sLst,opening+1,closing)
            sLst.pop()
            sLst.append(')')
            rec(n,sLst,opening,closing+1)
            sLst.pop()
        #endregion

        rec(n,[],0,0)
        return lst
#endregion











#region interesting online solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        @functools.cache
        def generate(n: int) -> List[str]:
            if n == 0: return ['']
            if n == 1: return ['()']

            result = []
            for x in range(n):
                for l in generate(x):
                    for r in generate(n-1-x):
                        result.append("(" + l + ")" + r)

            return result

        return generate(n)
#endregion

#region brute force
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(lst)->bool:
            stack = []
            for c in lst:
                if c == ')':
                    if stack and stack[-1] == ')':
                        return False
                    elif stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        # empty stack case
                        return False
                elif c == '(':
                    stack.append(c)
            # stack must be empty at the end
            return not stack

        def permute(lst,start,end)->None:
            nonlocal st
            if start == end:
                if isValid(lst):
                    st.add(''.join(lst))
                return
            for i in range(start,end):
                lst[i],lst[start] = lst[start],lst[i]
                permute(lst,start+1,end)
                # undo most recent swap
                lst[i],lst[start] = lst[start],lst[i]
        lst = ['(']*n + [')']*n
        # print(lst)
        st = set()
        permute(lst,0,len(lst))
        return list(st)
#endregion

