class Solution:
    '''
            [5,3,3,3,5,6,2] time = 2
    nonInc: [0,1,2,3,0,0,1]
    nonDec: [0,4,3,2,1,0,0]
            
            [1,4,7,5,2,3,4,6,5,5,6,7,8] time = 2
    nonInc: [0,0,0,1,2,0,0,0,1,2,0,0,0]
    nonDec: [2,1,0,0,3,2,1,0,4,3,2,1,0]
    [4,9]
    
    [2,1,2] time = 1
    nonInc: [0,1,0]
    nonDec: [0,1,0]
    
    [2,3,2] time = 1
    nonInc: [0,0,1]
    nonDec: [1,0,0]
    '''
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        # non increasing
        dp1 = [0]*n
        # non decreasing
        dp2 = [0]*n
        for i in range(1,n):
            if security[i] <= security[i-1]:
                dp1[i] = dp1[i-1] + 1
                
        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                dp2[i] = dp2[i+1] + 1
        # print(dp1)
        # print(dp2)
        # both values from the dp array must be at least time days 
        return [i for i,(x,y) in enumerate(zip(dp1,dp2)) if x >= time and y >= time]
        
        
        
