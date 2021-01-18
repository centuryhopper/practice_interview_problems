import numpy as np


class Solution:

    def __init__(self):
        self.vowels = np.array(['a', 'e', 'i', 'o', 'u'])

    def helper(self, n, vowel_ind) -> int:

        if n == 0:
            return 1

        res = 0

        # don't want to look back,
        # so start at the current vowel index
        for i in range(vowel_ind, self.vowels.size):

            # pass in current vowel we are iterating
            # over and recurse on that
            res += self.helper(n-1, i)

        return res

    def countVowelStrings(self, n: int) -> int:
        return self.helper(n, 0)
