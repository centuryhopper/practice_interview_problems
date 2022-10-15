'''
'abcde' 'ace'
   '' a b c d e
'' 0  0 0 0 0 0
a  0  1 1 1 1 1
c  0  1 1 2 2 2
e  0  1 1 2 2 3
'''
import pprint
import sys
from typing import Tuple

def longestCommonSubsequence(a: str, b: str) -> int:
    m,n = len(a),len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    # tuple(int,int) : tuple(int,int)
    parent = {}
    # DIAGONAL: matching character, so append it to both traceback strings
    # LEFT: mismatch, but this is a new character for the n string and the same character for the m string, so append character to n string and append a '-' to the m string
    # UP: mismatch, but this is a new character for the m string and the same character for the n string, so append character to m string and append a '-' to the n string
    lookup = {
        (-1,-1): 'DIAGONAL',
        (0,-1): 'LEFT',
        (-1,0): 'UP'
    }

    # init first column values
    for i in range(1,m+1):
        parent[(i,0)] = (i-1,0)
    # init first row values
    for i in range(1,n+1):
        parent[(0,i)] = (0,i-1)


    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                parent[(i,j)] = (i-1,j-1)
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if dp[i-1][j] > dp[i][j-1]:
                    parent[(i,j)] = (i-1,j)
                else:
                    parent[(i,j)] = (i,j-1)
    # pprint.pprint(parent)
    # pprint.pprint(dp)

    def traceback(i,j,s1,s2) -> Tuple[str,str]:
        if i == 0 and j == 0:
            return s1+'$'+s2
        nextI, nextJ = parent[(i,j)]
        # print(nextI,nextJ)
        direction = lookup[(nextI-i,nextJ-j)]
        if direction == 'DIAGONAL':
            s1Append = a[i-1] if i > 0 else ''
            s2Append = b[j-1] if j > 0 else ''
            return traceback(nextI,nextJ,s1Append+s1,s2Append+s2)
        if direction == 'LEFT':
            s2Append = b[j-1] if j > 0 else ''
            return traceback(nextI,nextJ,'-'+s1,s2Append+s2)
        if direction == 'UP':
            s1Append = a[i-1] if i > 0 else ''
            return traceback(nextI,nextJ,s1Append+s1,'-'+s2)

    final = traceback(m,n,'','')
    # print(final.split('$'))
    return dp[m][n]



longestCommonSubsequence(sys.argv[1], sys.argv[2])







































    # @lru_cache(None)
    # def rec(i,j) -> int:
    #     if i == len(a):
    #         return 0
    #     if j == len(b):
    #         return 0
    #     # match
    #     if a[i] == b[j]:
    #         return 1 + rec(i+1,j+1)
    #     # no match
    #     return max(rec(i+1,j), rec(i,j+1))

    # return rec(0,0)