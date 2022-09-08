class Solution:
    '''
    average case (insertion in the middle):
    intervals: [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new intervals: [4,8]
    output: [[1,2],[3,10],[12,16]]
    
    
    left outlier edge case:
    intervals: [[3,5],[6,7],[8,10],[12,16]]
    new intervals: [1,2]
    output: [[1,2],[3,5],[6,7],[8,10],[12,16]]
    
    
    right outlier edge case:
    intervals: [[3,5],[6,7],[8,10],[12,16]]
    new intervals: [17,18]
    output: [[3,5],[6,7],[8,10],[12,16],[17,18]]
    
    
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lb,ub = newInterval
        tmp = [lb,ub]
        ans = []
        pos = -1
        for i,(x,y) in enumerate(intervals):
            if x <= lb <= y:
                tmp[0] = x
                pos = i
            if x <= ub <= y:
                tmp[1] = y
            # not in range
            elif ub < x or y < lb:
                ans.append([x,y])
        
        ans.insert(pos,tmp)
        # return ans
        return sorted(ans, key=lambda x:x[0])
        
        
        
