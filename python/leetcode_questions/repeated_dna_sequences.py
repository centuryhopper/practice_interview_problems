from typing import List


# high-level idea (unoptimized)
def findRepeatedDnaSequences(self, s: str) -> List[str]:
    if len(s) < 10:
      return []
    seen = set()
    ans = []
    n, m = len(s), 10
    for i in range(n - m + 1):
        end = min(i + m, n)
        # print(s[i:end])
        if s[i:end] in seen:
            ans.append(s[i:end])
        else:
            seen.add(s[i:end])

    return ans


# link: https://leetcode.com/problems/repeated-dna-sequences/description/


# memory-efficient Solution
class Solution:
    # high-level idea (unoptimized)
    # save every substring in a set and check for repeats

    """
    A -> 01
    C -> 10
    G -> 00
    T -> 11

    mapping = {
        'A' : 1,
        'C' : 2,
        'G' : 0,
        'T' : 3,
    }

    AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT

    AAAAACCCCC
    10101010100101010101

    AAAACCCCCA
    01101010101001010101

    AAACCCCCAA
    01011010101010010101

    'A' : 1,
    'C' : 2,
    'G' : 0,
    'T' : 3,
    """

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {
            "A": 1,
            "C": 2,
            "G": 0,
            "T": 3,
        }

        def make_hash(chunk):
            state = 0
            # reversed so that dropping the trailing two bits of the hash is equivalent to dropping the leading character of the 10-character string
            for ch in chunk[::-1]:
                state |= mapping[ch]
                state <<= 2
            # undo the last shift (edge case)
            state >>= 2
            return state

        if len(s) < 10:
            return []
        ans = []
        n, m = len(s), 10
        initialChunk = s[:m]
        curHash = make_hash(initialChunk)
        # print(curHash)
        seen = set([curHash])
        strLst = list(initialChunk)
        for i in range(10, n):
            ch = s[i]
            strLst.append(ch)
            strLst = strLst[1:]
            # remove the trailing two bits (again this is equivalent to removing the leading character of the chunk in the sliding window)
            curHash >>= 2
            twoBit = mapping[ch]
            twoBit <<= 18
            # add the trailing character into the int
            curHash |= twoBit
            if curHash in seen:
                ans.append("".join(strLst))
            seen.add(curHash)
        # print(seen)
        return ans



