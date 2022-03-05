from typing import List
from collections import Counter

class Solution:
    '''
    [1,2]
    4
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def rec(candidates, target, curSum, path):
            nonlocal ans
            if curSum > target:
                return
            if curSum == target:
                curPathCnter = Counter(path)
                for lst in ans:
                    # slow but works
                    if Counter(lst) == curPathCnter:
                        return
                ans.append(path.copy())
                return
            for candidate in candidates:
                rec(candidates,target,curSum+candidate,path+[candidate])

        rec(candidates, target, 0, [])
        return ans







