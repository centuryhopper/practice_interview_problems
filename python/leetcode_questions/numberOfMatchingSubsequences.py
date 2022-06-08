from collections import deque, defaultdict
import bisect
#region interesting solution by tim https://www.youtube.com/watch?v=9zzDQJLcY9Y

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = defaultdict(list)
        output = 0
        for i,c in enumerate(s):
            lookup[c].append(i)
        for w in words:
            prev = -1
            found = True
            for c in w:
                tmp = bisect.bisect(lookup[c], prev)
                if tmp == len(lookup[c]):
                    found = False
                    break
                else:
                    prev = lookup[c][tmp]
            if found:
                output += 1
        return output
#endregion




#region finally working code


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = {c:deque() for c in s}
        cnt = 0
        # add each word by their first character
        for word in words:
            first = word[0]
            # if character doesn't exist in dictionary, then continue
            if first not in d: continue
            d[first].append(word)
        # remove the first letter of every word in character's corresponding list
        for c in s:
            q = d[c]
            size = len(q)
            # a traditional for loop is necessary here instead of
            # a for-in loop because we're appending within that loop
            for i in range(size):
                word = q.popleft()
                if not word[1:]:
                    cnt+=1
                else:
                    if word[1] in d:
                        d[word[1]].append(word[1:])
        return cnt
#endregion


# region brute force (TLE)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSub(a: str, b: str) -> bool:
            if len(a) > len(b):
                return False
            bIter = iter(b)
            return all(c in bIter for c in a)

        return sum(1 for word in words if isSub(word, s))
# endregion


#region failed attempt
# from collections import defaultdict

# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         d = {c:[] for c in s}
#         cnt = 0
#         # add each word by their first character
#         for word in words:
#             first = word[0]
#             # if character doesn't exist in dictionary, then continue
#             if first not in d: continue
#             d[first].append(word)
#         # remove the first letter of every word in character's corresponding list
#         for c in s:
#             wordsToRemove = []
#             for word in d[c]:
#                 shortenedWord = word[1:]
#                 # found a subsequence
#                 if not shortenedWord:
#                     cnt+=1
#                     wordsToRemove.append(word)
#                     continue
#                 # add to another part of dictionary if newWord's first letter no longer matches that of c
#                 if shortenedWord[0] != c:
#                     # remove word from d[c]
#                     wordsToRemove.append(word)
#             # words that were marked for removal in the previous loop
#             for word in wordsToRemove:
#                 d[c].remove(word)
#                 if len(word) == 1: continue
#                 first = word[1]
#                 if first in d:
#                     d[first].append(word[1:])

#             # print(d)
#             # print()

#         print(d)
#         return cnt
#endregion