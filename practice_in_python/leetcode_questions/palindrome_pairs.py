from collections import defaultdict
# inspired by https://www.youtube.com/watch?v=ewNE1UbjmJ8

# time: O(n * k^2) where n is the length of words and k is the length of the longest string
# space: O(n) because of our dictionary d varying with respect to the length of words
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalin(s) -> bool: return s == s[::-1]
        ret = []
        # default value is -1
        d = defaultdict(lambda: -1, {word: i for i, word in enumerate(words)})
        # handle empty string case
        # all palindrome strings will be paired
        # with empty string
        if '' in d:
            emptyStrIndex = d['']
            for i, word in enumerate(words):
                if i != emptyStrIndex and isPalin(word):
                    ret.extend([[emptyStrIndex, i], [i, emptyStrIndex]])
        # handle reversed string case
        for i, word in enumerate(words):
            reversedIndex = d[word[::-1]]
            # if the reversed string exists
            # and isn't the current string
            # we're iterating over
            if reversedIndex != -1 and reversedIndex != i:
                ret.append([i, reversedIndex])
            # handle substring case
            # if one of the string pieces is a palindrome
            # and the the reverse of the other is in the list then
            # ret.append([d[reversed(other half)], d[half]])
            for j in range(1, len(word)):
                left = word[:j]
                right = word[j:]
                if isPalin(left) and d[right[::-1]] != -1:
                    ret.append([d[right[::-1]], i])
                if isPalin(right) and d[left[::-1]] != -1:
                    ret.append([i, d[left[::-1]]])
        return ret
