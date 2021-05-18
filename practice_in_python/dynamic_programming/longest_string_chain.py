


# inefficient solution
# from collections import defaultdict
# class Solution:

#     def longestStrChain(self, words: List[str]) -> int:
#         # sort by length in ascending order
#         words.sort(key=lambda w:len(w))
#         # print(words)
#         res, n = 1, len(words)
#         # all 1's because every value could potentially be taken by itself
#         d = defaultdict(lambda:1)
#         for i,word in enumerate(words):
#             if len(word) == 1:
#                 continue
#             for idx in range(len(word)):
#                 subWord = word[:idx] + word[idx+1:]

#                 # find the word that matches the subword
#                 for j in range(i):
#                     if words[j] == subWord:
#                         d[word] = max(d[word], d[subWord] + 1)
#                         res = max(res,d[word])


#         return res







# inefficient solution
# class Solution:
#     # len(a) <= b
#     # e.g. ac, abc => true
#     def is_sub(self, a,b) -> bool:
#         if len(a) > len(b): return False
#         it = iter(b)
#         return all(c in it for c in a)

#     def longestStrChain(self, words: List[str]) -> int:
#         # sort by length in descending order
#         words.sort(key=lambda w:len(w))
#         # print(words)
#         res, n = 1, len(words)
#         # all 1's because every value could potentially be taken by itself
#         dp = [1] * n
#         for i in range(n):
#             if len(words[i]) == 1:continue
#             for j in range(i):
#                 if self.is_sub(words[j], words[i]) and len(words[j])+1==len(words[i]):
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     res = max(res, dp[i])
#         return res












'''
failed attempt
class Solution:
    # len(a) <= b
    # e.g. ac, abc => true
    def is_sub(self, a,b) -> bool:
        if len(a) > len(b): return False
        it = iter(b)
        return all(c in it for c in a)

    def rec(self, words, cur) -> int:
        if cur == len(words) - 1: return 1
        res = 1
        for i in range(cur+1, len(words)):
            # find a word that is one character less than current word and
            # is a subsequence of it. We can choose to recurse on it or skip it
            # skip words of the same length
            if len(words[i]) == len(words[cur]): continue
            # no need to continue searching bc words are too small
            if len(words[i]) + 1 < len(words[cur]): break
            if self.is_sub(words[i], words[cur]):
                take = 1 + self.rec(words,i)
                res = max(res,take)
        # print(res, words[cur])
        return res


    def longestStrChain(self, words: List[str]) -> int:
        # sort by length in descending order
        words.sort(key=lambda w:-len(w))
        # print(words)

        return self.rec(words, 0)


'''