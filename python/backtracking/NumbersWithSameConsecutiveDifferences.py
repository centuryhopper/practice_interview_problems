class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def backtrack(path:str):
            if len(path) == n:
                ans.append(int(path))
                return
            for i in range(10):
                if abs(int(path[-1]) - i) == k:
                    backtrack(path+f'{i}')
            
        # always looking ahead for the next possible digit 
        for i in range(1,10):
            backtrack(str(i))
        
        return ans
