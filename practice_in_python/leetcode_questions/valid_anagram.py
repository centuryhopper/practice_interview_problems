
from collections import defaultdict


class Solution:

    # frequency must be 0 in the end when looping thru both strings
    # def isAnagram(self, s: str, t: str) -> bool:

    # if len(s) != len(t):
    #     return False
    # d = defaultdict(int)

    # # record frequency for first string
    # for ch in s:
    #     d[ch] += 1

    # # record frequency for second string
    # for ch in t:
    #     d[ch] -= 1
    #     # we can leave early if there are more occurrences of a particular letter
    #     # in t
    #     if d[ch] < 0:
    #         return False

    # # if the number of letters match in both strings,
    # # then the value of every key should be 0
    # for val in d.values():
    #     if val > 0:
    #         return False
    # return True

    def isAnagramOptimized(self, s: str, t: str) -> bool:
        return {k: s.count(k) for k in set(s)} == {
            k: t.count(k) for k in set(t)}


def isAnagramOptimized(s: str, t: str) -> bool:

    # print(set(s))
    # print(set(t))

    # remove duplicates then add each letter to a dictionary with
    # the key being the letter and the value being the frequency of
    # that letter in the original string (this solution is so clever)
    a = {k: s.count(k) for k in set(s)}
    b = {k: t.count(k) for k in set(t)}

    print(a)
    print(b)

    return {k: s.count(k) for k in set(s)} == {k: t.count(k) for k in set(t)}


if __name__ == '__main__':
    print(isAnagramOptimized('leo', 'loe'))
