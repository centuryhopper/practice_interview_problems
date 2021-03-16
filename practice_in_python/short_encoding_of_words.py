


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encoded = set(words)

        # remove substring words from the set
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in encoded:
                    encoded.remove(word[i:])

        # print('#'.join(encoded))

        # + 1 to account for the final hashtag
        return len('#'.join(encoded)) + 1


    # TODO: implement a trie to solve this problem
