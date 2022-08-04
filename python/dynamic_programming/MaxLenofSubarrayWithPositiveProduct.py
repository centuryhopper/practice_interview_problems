class Solution:
    '''
    [0,-1,-2,3,0,1,-2,4,-1,-5,-6,-7,0,5,0]
    
    split array into subarrays
    split at every 0
    
    now every subarray with an even number of negative values
    don't need extra processing
    
    [ [-1,-2,3],[1,-2,4,-1,-5,-6,-7],[5] ]
    
    
    '''
    def getMaxLen(self, nums: List[int]) -> int:
        # sub-arrays
        subs = []
        tmp = []
        for num in nums:
            if num == 0:
                if tmp:
                    subs.append(tmp)
                    tmp = []
            else:
                tmp.append(num)
        # handle trailing subarray with not split by 0's
        # e.g. [1,-2,-3,4] or [0,1,-2,-3,-4]
        if tmp:
            subs.append(tmp)
        # print(subs)
        
        ans = 0
        for sub in subs:
            # track the first and last negative values' indices
            first = last = None
            negs = 0
            for i,num in enumerate(sub):
                if num < 0:
                    if first is None:
                        first = i
                    last = i
                    negs+=1
                        
            if negs % 2 == 0:
                ans = max(ans,len(sub))
            else:
                # handle odd number of negatives
                # trim from left until we trim our first negative
                n = len(sub)
                left = n - first - 1
                # trim from right until we trim our first positive
                right = last
                ans = max(ans,left,right)
                
        
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
