class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        # all zeroes can be safely counted
        ans += s.count('0')
        mult = 1
        # total value of the ones found
        ones = 0
        for i in range(n-1,-1,-1):
            if s[i] == '1' and ones <= k:
                ones += mult
                # don't include this value of one to our answer size since otherwise it's larger than k
                if ones > k:
                    break
                ans += 1
            mult *= 2
        return ans
                
        
        
        
        
        
        
        
        
        
        
        
        
