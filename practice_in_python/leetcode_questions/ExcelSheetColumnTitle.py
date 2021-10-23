class Solution:
    '''
    1 => 1 + 65 - 1 => A
    1-26 => A-Z
    27-52 => AA-AZ
    53-78 => BA-BZ

    78 =>
    78 % 26 = 0 => Z
    (78 / 26) - 1 = 2
    2 % 26 = 2 => B

    783 =>
    783 % 26 => 3 => C
    (783 / 26) = 30
    30 % 26 => 4 => D
    (30 / 26) = 1
    1 % 26 = 1 => A
    1 / 26 = 0 DONE
    '''
    def convertToTitle(self, cn: int) -> str:
        # only works for 1-26, inclusive
        numberToLetter = lambda n: chr(n+65-1) if n > 0 else 'Z'
        ans = ''
        while cn > 0:
            letterNum = cn%26
            ans = numberToLetter(letterNum) + ans
            cn = cn//26 if letterNum != 0 else (cn//26)-1
        return ans

