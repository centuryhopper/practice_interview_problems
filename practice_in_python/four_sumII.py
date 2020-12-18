class Solution:

# O(n^2) solution
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        # keep a cnt of the total number of possible sums
        retVal = 0
        m = {}

        # find all possible sums and save to the hash map
        for c in C:
            for d in D:
                res = c + d
                m[res] = m[res] + 1 if res in m else 1


        # check for complements in the other two arrays
        for a in A:
            for b in B:
                res = a + b
                retVal = retVal + m[-res] if -res in m else retVal

        return retVal

        