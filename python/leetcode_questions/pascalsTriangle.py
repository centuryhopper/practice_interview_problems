class Solution:
    '''
    						1
                         1     1
                       1    2    1
                      1   3   3   1
                      ...etc
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            tmp = []
            for j in range(0,i+1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(ret[i-1][j-1] + ret[i-1][j])
            ret.append(tmp)

        return ret



