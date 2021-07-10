

#region brute force
class Solution:
    # need to have an even number of zeros
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        if n & 1 or n<=0: return False
        cntZeros = 0
        cntOnes = 0
        while n > 0:
            if not (n&1):
                cntZeros+=1
            else:
                cntOnes+=1
            n>>=1
        # print(cntZeros,cntOnes)
        # make sure there are an even number of zeros
        return not (cntZeros & 1) and cntOnes==1
#endregion

#region optimized
from math import log

class Solution:
    # need to have an even number of zeros
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n) / log(4) % 1 == 0

#endregion