class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        l = 2
        for r in range(2, len(a)):
            if a[l - 2] != a[r]:
                a[l], l = a[r], l + 1
        return l
