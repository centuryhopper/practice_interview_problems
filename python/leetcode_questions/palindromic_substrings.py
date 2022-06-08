class Solution:

    def rec(self,s:str, i:int, j:int) -> int:
        if i >= len(s):
            return 0
        if i == j:
            return self.rec(s,i+1, len(s))
        if s[i:j] == s[i:j][::-1]:
            return 1 + self.rec(s,i,j-1)
        return self.rec(s,i,j-1)

    def rec_memo(self,s:str, i:int, j:int, memo) -> int:
        if i >= len(s):
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if i == j:
            memo[i][j] = self.rec_memo(s,i+1, len(s), memo)
            return memo[i][j]
        if s[i:j] == s[i:j][::-1]:
            memo[i][j] = 1 + self.rec_memo(s,i,j-1, memo)
            return memo[i][j]
        memo[i][j] = self.rec_memo(s,i,j-1, memo)
        return memo[i][j]

    def dp_solution(self, s:str, dpAr:list[list[int]]) -> int:

#         for i in range(len(s), -1, -1):
#             for j in range(len(s)+1):


        return

    # TODO code up dynamic programming tabular approach
    def countSubstrings(self, s: str) -> int:

        # memo = [[-1]*(len(s)+1) for _ in range(len(s)+1)]
        # return self.rec_memo(s,0,len(s), memo)
        dpAr = []
        for i in range(len(s)+1):
            dpAr.append([])
            for j in range(len(s)+1):
                dpAr[i].append(1 if i == j else 0)
        # print('\n'.join('{}: {}'.format(*k) for k in enumerate(dpAr)))
        return

        