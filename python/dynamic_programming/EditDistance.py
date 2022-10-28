import sys
import pprint
from typing import Tuple

def minDistance(a: str, b: str) -> int:
    m,n = len(a),len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    # base cases
    dp[0][0] = 0

    parent = {}
    lookup = {
        (-1,-1): 'REPLACE',
        (0,-1): 'INSERT',
        (-1,0): 'REMOVE'
    }

    for i in range(1,m+1):
        parent[(i,0)] = (i-1,0)
    # init first row values
    for i in range(1,n+1):
        parent[(0,i)] = (0,i-1)

    for i in range(1,m+1):
        dp[i][0] = i
    for i in range(1,n+1):
        dp[0][i] = i

    for i in range(1,m+1):
        for j in range(1,n+1):
            # if match then take minimum of left+1,up+1, and diagonal
            # otherwise take the minimum of left+1,up+1, and diagonal+1
            left = dp[i][j-1]
            up = dp[i-1][j]
            diagonal = dp[i-1][j-1]
            if a[i-1] == b[j-1]:
                dp[i][j] = diagonal
                parent[(i,j)] = (i-1,j-1)
            else:
                if i == m:
                    print(a[i-1], b[j-1])
                dp[i][j] = min(left,up,diagonal)+1
                if left < up and left < diagonal:
                    parent[(i,j)] = (i,j-1)
                elif up < left and up < diagonal:
                    parent[(i,j)] = (i-1,j)
                else:
                    parent[(i,j)] = (i-1,j-1)

    # pprint.pprint(parent)
    pprint.pprint(dp)

    def traceback(i,j,s1,s2) -> Tuple[str,str]:
        if i == 0 and j == 0:
            return s1+'$'+s2
        nextI, nextJ = parent[(i,j)]
        # print(nextI,nextJ)
        direction = lookup[(nextI-i,nextJ-j)]
        if direction == 'REPLACE':
            s1Append = a[i-1] if i > 0 else ''
            s2Append = b[j-1] if j > 0 else ''
            return traceback(nextI,nextJ,s1Append+s1,s2Append+s2)
        if direction == 'INSERT':
            s2Append = b[j-1] if j > 0 else ''
            return traceback(nextI,nextJ,'-'+s1,s2Append+s2)
        if direction == 'REMOVE':
            s1Append = a[i-1] if i > 0 else ''
            return traceback(nextI,nextJ,s1Append+s1,'-'+s2)

    final = traceback(m,n,'','')
    print(final.split('$'))



    return dp[m][n]



# ans = minDistance("horse", "ros")
#print(ans)
# ans = minDistance("acta", "agag")
print(minDistance(sys.argv[1],sys.argv[2]))


