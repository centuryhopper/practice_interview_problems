
class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        # assumes word and pat are the same length
        def isMatch(word, pat) -> bool:
            wordToPat = [0]*26
            patToWord = [0]*26
            for i in range(len(word)):
                wordLetter = word[i]
                patLetter = pat[i]
                if patToWord[ord(patLetter) - ord('a')] == 0:
                    patToWord[ord(patLetter) - ord('a')] = wordLetter
                if wordToPat[ord(wordLetter) - ord('a')] == 0:
                    wordToPat[ord(wordLetter) - ord('a')] = patLetter

                # find mismatches
                if patToWord[ord(patLetter) - ord('a')] != wordLetter or wordToPat[ord(wordLetter) - ord('a')] != patLetter:
                    return False
            return True

        return [word for word in words if isMatch(word, pattern)]



        