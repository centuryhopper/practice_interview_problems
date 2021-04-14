class Solution:
    def kWeakestRows(self, lst: List[List[int]], k: int) -> List[int]:
        lst = list(enumerate(lst))
        lst.sort(key=lambda x: x[1].count(1))
        return [lst[i][0] for i in range(k)]
    
