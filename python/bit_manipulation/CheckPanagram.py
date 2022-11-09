class Solution:
    '''
    1101
    1111
    ----
    0010 => False
    
    '''
    def checkIfPangram(self, sentence: str) -> bool:
        # the bitmask xorred with 1 should be 0. Otherwise return false
        bitmask = 0
        for c in sentence:
            bitmask |= (1 << ord(c)-97)
        # (2^26) - 1 => 26 ones
        return bitmask ^ ((2**26) - 1) == 0
        
