



class Solution:
    '''
    5 => 101
    0 + 1*0 = 0
    0 + 2*1 = 2
    2 + 4*0 = 2
    ans = 2 => 010
    '''
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        ans = 0
        mult = 1
        while n > 0:
            ans += mult*(0 if 1 & n else 1)
            mult*=2
            n>>=1
        return ans



