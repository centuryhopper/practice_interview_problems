https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution:
    '''
    lets pretend we're only solving for one side of the
    street:
    if n == 0:
        *1 possibility => no placement at all
    if n == 1:
        *2 possibility => house is placed in the hole or not placed at all
    if n == 2:
        *3 possibilities => 
        house is placed in hole 1
        house is placed in hole 2
        house is not placed at all
    if n == 3:
        *5 possibilities =>
        house is placed in left one
        house is placed in middle one
        house is placed in right one
        two houses, one placed in left and the other in right
        no placement at all
    
    etc... similar to fibonacci looking at the pattern that I starred with an asterisk
    to include the other side of the street, we'll square our answer derived from one side
    '''
    
    
    def countHousePlacements(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 2
        MOD = 7 + 10**9
        for i in range(2,n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        return (dp[n]*dp[n]) % MOD
        
