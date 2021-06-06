class Solution:

    def rec(self,s1,s2,s3,i,j,k) -> bool:
        if i == len(s1) and j == len(s2) and k == len(s3): return True
        if k == len(s3): return False

        # one finishes before the other
        if i == len(s1):
            if j == len(s2) or s2[j] != s3[k]:
                return False
            return self.rec(s1,s2,s3,i,j+1,k+1)
        if j == len(s2):
            if i == len(s1) or s1[i] != s3[k]:
                return False
            return self.rec(s1,s2,s3,i+1,j,k+1)

        if s3[k] == s1[i] and s3[k] == s2[j]:
            # try both
            return self.rec(s1,s2,s3,i+1,j,k+1) or self.rec(s1,s2,s3,i,j+1,k+1)
        if s3[k] == s1[i]:
            return self.rec(s1,s2,s3,i+1,j,k+1)
        if s3[k] == s2[j]:
            return self.rec(s1,s2,s3,i,j+1,k+1)

        return False

    def rec_memo(self,s1,s2,s3,i,j,k,memo) -> bool:
        key = (i,j,k)
        if key in memo:
            return memo[key]
        if i == len(s1) and j == len(s2) and k == len(s3): return True
        if k == len(s3): return False

        # one finishes before the other
        if i == len(s1):
            if j == len(s2) or s2[j] != s3[k]:
                return False
            memo[key] = self.rec_memo(s1,s2,s3,i,j+1,k+1,memo)
            return memo[key]
        if j == len(s2):
            if i == len(s1) or s1[i] != s3[k]:
                return False
            memo[key] = self.rec_memo(s1,s2,s3,i+1,j,k+1,memo)
            return memo[key]

        if s3[k] == s1[i] and s3[k] == s2[j]:
            # try both
            memo[key] = self.rec_memo(s1,s2,s3,i+1,j,k+1,memo) or self.rec_memo(s1,s2,s3,i,j+1,k+1,memo)
            return memo[key]
        if s3[k] == s1[i]:
            memo[key] = self.rec_memo(s1,s2,s3,i+1,j,k+1,memo)
            return memo[key]
        if s3[k] == s2[j]:
            memo[key] = self.rec_memo(s1,s2,s3,i,j+1,k+1,memo)
            return memo[key]

        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.rec_memo(s1,s2,s3,0,0,0,{})



