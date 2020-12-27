class Solution:
    def smallestRangeII(self, a: List[int], K: int) -> int:
        if len(a) <= 1: return (a[0] + K) - (a[0] - K)

        # make sure the array is sorted first
        a.sort()
        n = len(a)

        # inital gap
        gap = a[n - 1] - a[0]

        for i in range(n - 1):
            j = i + 1
            
            hi = max(a[n - 1] - K, a[i] + K)
            low = min(a[0] + K, a[j] - K)
            gap = min(gap, hi - low)

        return gap