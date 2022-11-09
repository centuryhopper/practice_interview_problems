import sys
import pprint

def isValidRNA_Pair(a,b) -> bool:
    a = a.upper()
    b = b.upper()
    return \
    (a == 'A' and b == 'U') or (a == 'G' and b == 'U') or (a == 'G' and b == 'C')\
    or\
    (b == 'A' and a == 'U') or (b == 'G' and a == 'U') or (b == 'G' and a == 'C')


def nussinov(RNA:str)->int:
    n = len(RNA)
    print(f'size of the input is {n}')
    dp = [[0]*n for _ in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            left = dp[i][j-1]
            down = dp[i+1][j]
            diagonalDown = dp[i+1][j-1]
            if isValidRNA_Pair(RNA[i], RNA[j]):
                dp[i][j] = diagonalDown + 1
            else:
                dp[i][j] = max(left, down, diagonalDown)
    
    #pprint.pprint(dp)
    for row in dp:
        print(dp)

    return dp[0][-1]

# AAUCUGUUACGCA
# GGGAAAUCC
# GAGCCAUUAGCUCAGUUGGUAGAGCAUCUGACUUUUAAUCAGAGGGUCGAAGGUUCGAGUCCUUCAUGGCUCA
print(nussinov(sys.argv[1]))

