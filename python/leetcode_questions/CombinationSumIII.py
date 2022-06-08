from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def rec(k,n,curSum,path,x):
            # global variable ans
            nonlocal ans

            # if sum is too high, terminate
            if curSum > n:
                return
            # found a valid path
            if k == 0 and curSum == n:
                ans.append(path)
                return
            # if exhausted all k and cursum isn't n, terminate
            if k == 0:
                return

            # try all possible combinations and backtrack
            for i in range(x,10):
                rec(k-1,n,curSum+i,path+[i],i+1)

        ans = []
        rec(k,n,0,[],1)
        # print(ans)
        return ans


