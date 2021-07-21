


#region my not so efficient solution
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lst = list(dominoes)
        n = len(lst)
        # handle R cases
        for i in range(n):           
            j = i+1
            if lst[i] == 'R':
                firstDot = -1
                lastDot = -1
                while j < n and lst[j] != 'R' and lst[j] != 'L':
                    if lst[j] == '.':
                        if firstDot == -1:
                            firstDot = j
                        lastDot = j
                    j+=1
                # R... case and R...R case
                if j >= n:
                    for x in range(i,j):
                        lst[x] = 'R'
                    break
                elif lst[j] == 'R':
                    for x in range(i,j):
                        lst[x] = 'R'
                # R...L case
                elif lst[j] == 'L':
                    while firstDot < lastDot:
                        lst[firstDot] = 'R'
                        lst[lastDot] = 'L'
                        firstDot+=1
                        lastDot-=1
        # handle L cases
        for i in range(n-1,-1,-1):
            j = i-1
            if lst[i] == 'L':
                cntDots = 0
                while j >= 0 and lst[j] != 'L' and lst[j] != 'R':
                    if lst[j]=='.': cntDots+=1
                    j-=1
                # no left bound
                if j < 0:
                    for x in range(i):
                        lst[x] = 'L'
                # previous for loop didn't handle these
                # make sure that there are vertical dominoes in between (dots) and that the left bound
                # isn't an R (so left bound must be an L in this case i.e. L...L etc)
                elif cntDots > 0 and lst[j] != 'R':
                    for x in range(j,i):
                        lst[x] = 'L'        
        return ''.join(lst)
#endregion