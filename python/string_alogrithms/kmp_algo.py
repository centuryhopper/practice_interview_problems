import time


class kmp:
    def kmpSearch(self, text: str, pat: str) -> list[int]:
        n = len(text)
        m = len(pat)
        # return value of all indices where the match is found
        matchIndices = []
        # lps array the size of the pattern
        lpsArray = [0 for _ in range(m)]
        self.__preprocessLPSArray(pat, lpsArray)
        # print(lpsArray)

        # i will scan thru the text string
        # j will scan thru the pattern string
        i, j = 0, 0
        while i < n:
            if text[i] == pat[j]:
                i += 1
                j += 1
            # if j traverses the whole pattern string,
            # then we've found a match at index i
            if j == m:
                matchIndices.append(i-j)

                # todo why this line???
                # because we are maping to the value at index previous to j
                # in case we can still find a pattern match.
                # if still find no match, then keep doing j = lpsArray[j-1]
                j = lpsArray[j-1]

            # mismatch
            elif i < n and pat[j] != text[i]:
                if j > 0:
                    # map j to the value at previous index
                    j = lpsArray[j-1]
                else:
                    # cannot move j any further, so increment i
                    i += 1
        return matchIndices

    # longest proper prefix which is also the suffix.
    # for example, given 'abc', 'ab' and 'a' are proper prefixes, but 'abc' is not
    # private method
    def __preprocessLPSArray(self, pat: str, lps: list[int]) -> None:

        # first element inside lpsArray is always 0
        lps[0] = 0

        i, j = 0, 1
        while j < len(pat):
            # matching character
            if pat[i] == pat[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i != 0:
                    # shift i to the lps[i-1]th index
                    i = lps[i-1]
                else:
                    lps[j] = 0
                    j += 1


if __name__ == '__main__':
    o = kmp()
    # t = 'ababcabcabababd'
    # p = 'ababd'
    t = 'The world is completely devastated with the amid breakout of coronavirus'
    p = 'coronavirus'
    t = 'abcxabcabcabbabbaaaabxabcabcabcabbbaababcabaa'
    p = 'abcabc'
    start = time.perf_counter()
    print(o.kmpSearch(t, p))
    end = time.perf_counter()
    print(f'kmp took {(end - start) * 1000} ms')
    start = time.perf_counter()
    print(t.find(p))
    end = time.perf_counter()
    print(f'python built-in index method took {(end - start) * 1000} ms')
