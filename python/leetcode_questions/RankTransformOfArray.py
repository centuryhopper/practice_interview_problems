class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []
        tmp = sorted(arr.copy())
        d = {tmp[0]:1}
        for i in range(1,len(arr)):
            if tmp[i] not in d:
                d[tmp[i]] = d[tmp[i-1]]+1
        return [d[num] for num in arr]
        