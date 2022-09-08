class Solution:
    '''
    1,2,3,4
    
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def rec(lst, cur, path):
            if len(path) == k:
                ans.append(path)
                return
            for i in range(cur, len(lst)):
                rec(lst,i+1, path+[lst[i]])
        rec(list(range(1,n+1)), 0, [])
        return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
