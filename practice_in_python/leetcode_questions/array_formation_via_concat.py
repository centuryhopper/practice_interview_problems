class Solution:

    '''b must be at least the size of a'''
    def isSubList(self, a: list[int], b: list[int]) -> bool:
        if len(a) > len(b):
            return False
        for i in range(0, len(b) - len(a) + 1):
            if b[i:i+len(a)] == a:
                return True
        return False

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        for p in pieces:
            if not self.isSubList(p, arr):
                return False
        return True

