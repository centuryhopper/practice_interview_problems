class Solution:
    '''
    The sum of chosen elements will not be too large. Consider using a hash set to record all possible sums while iterating each row.
    
Instead of keeping track of all possible sums, since in each row, we are adding positive numbers, only keep those that can be a candidate, not exceeding the target by too much.

[[3,5],[4,4],[1,7],[1,1]]
67
    '''
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # i will use memoization
        memo = {}
        m,n = len(mat), len(mat[0])
        def rec(i, curSum):
            if (i, curSum) in memo:
                return memo[(i,curSum)]
            if i == m:
                return abs(curSum-target)
            minn = math.inf
            for num in mat[i]:
                minn = min(minn,rec(i+1, curSum+num))
                # leave the loop early when the current sum has already exceeded the target
                # We do this after making the call so that we still get our answer returned
                if curSum + num >= target:
                    break
            memo[(i,curSum)] = minn
            return minn
        
        # sort and remove duplicates at each row
        for i in range(m):
            mat[i] = sorted(set(mat[i]))
            
                
        return rec(0,0)
    
    
