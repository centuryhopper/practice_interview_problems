class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda i: i ** 2, nums)))
