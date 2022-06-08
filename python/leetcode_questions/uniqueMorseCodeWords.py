class Solution:
    # time: O(N*k)
    # space: O(N)
    # N is the size of input words array and k is average length of each word in words
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        # prep key mapping
        lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ret = set()
        # translate characters into morse code
        for word in words:
            s = ''
            for c in word:
                s += lst[ord(c)-97]
            ret.add(s)
        
        
        return len(ret)
        
        
        