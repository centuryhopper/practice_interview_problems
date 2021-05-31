from collections import defaultdict


class Solution:

    # brute force approach: pattern match one string with every other string in the array
    # O(n * n * l * l), where n is the number of words and l is the length of the longest word

    # my optimized state approach. time: O(n^2), space: O(n), where n is the number of words
    def maxProduct(self, words: List[str]) -> int:
        def setNthBit(dic, i, n):
            dic[i] |= (1 << n)

        # create dict with key as the index of the string
        # and value as the current state initialized to zero
        d = defaultdict(int)

        for i, word in enumerate(words):
            for c in word:
                setNthBit(d, i, ord(c)-97)

        maxVal = 0
        l = list(d.items())
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                # if they have no letters in common
                if l[i][1] & l[j][1] == 0:
                    ind1 = l[i][0]
                    ind2 = l[j][0]
                    maxVal = max(maxVal, len(words[ind1]) * len(words[ind2]))
        return maxVal
