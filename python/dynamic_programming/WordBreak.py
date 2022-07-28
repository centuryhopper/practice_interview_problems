from typing import Dict, List

class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children : Dict[str,TrieNode] = {}

class Trie:
    '''
    didn't create a delete for the sake of time
    '''
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word:str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = TrieNode()
            tmp = tmp.children[c]
        tmp.isEndOfWord = True
    def contains(self,word:str) -> bool:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                # print('here')
                return False
            tmp = tmp.children[c]
        return tmp.isEndOfWord




class Solution:
    '''
      c   a   t   s   a   n   d   o   g
    +-----------------------------------+
  c | f | f | t | t | f | f | t | f | F |
    +-----------------------------------+
  a | f | f | f | f | f | f | f | f | f |
    +-----------------------------------+
  t | f | f | f | f | f | f | f | f | f |
    +-----------------------------------+
  s | f | f | f | f | f | f | t | f | f |
    +-----------------------------------+
  a | f | f | f | f | f | f | f | f | f |
    +-----------------------------------+
  n | f | f | f | f | f | f | f | f | f |
    +-----------------------------------+
  d | f | f | f | f | f | f | f | f | t |
    +-----------------------------------+
  o | f | f | f | f | f | f | f | f | f |
    +-----------------------------------+
  g | f | f | f | f | f | f | f | f | f |
    +-----------------------------------+


    sandog is false not only bc its not in the wordDict, but also bc you can't split the words in any way such that it works
      s   a   n   d   o   g
    +-----------------------+
  s | F | F | F | T | F | F |
    +-----------------------+
  a |   | F | F | T | F | F |
    +-----------------------+
  n |   |   | F | F | F | F |
    +-----------------------+
  d |   |   |   | F | F | T |
    +-----------------------+
  o |   |   |   |   | F | F |
    +-----------------------+
  g |   |   |   |   |   | F |
    +-----------------------+

    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        # allow for faster look up times
        # didn't feel like building a trie
        # wordDict = set(wordDict)

        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        # print(trie.contains('leet'))

        # handle diagonals
        for i in range(n):
            if trie.contains(s[i]):
                dp[i][i] = True

        # bottom up
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if trie.contains(s[i:j+1]):
                    dp[i][j] = True
                else:
                    # find the split point that works
                    for x in range(i,j):
                        # check if the string up the xth index is splittable or in the word dict
                        if dp[i][x]:
                            # check if the other piece of the split is splittable or in the word dict
                            if dp[x+1][j]:
                                dp[i][j] = True
        # for row in dp:
        #     print(row)
        return dp[0][n-1]























