class Solution:

    # return the index of mid once it equals lo
    # because we can traverse from mid up to the first occurrence of a word that doesn't match
    # our prefix or when we already just added 3 into our trie (whichever one comes first)
    def bin_search(self, products: list[str], prefix: str) -> int:
        lo, hi = 0, len(products) - 1
        # no need to worry about int overflow in other languages because len(products) <= 1000
        prefixSize = len(prefix)
        mid = (lo + hi) // 2
        while lo != mid:
            curString = products[mid]
            if curString[:prefixSize] < prefix:
                lo = mid
            elif curString[:prefixSize] >= prefix:
                hi = mid
            # recalculate mid
            mid = (lo + hi) // 2
        return mid

    # store the best 3 words into the trie
    class Trie:
        def __init__(self):
            self.root = TrieNode()
            self.lst = []

        # gets all words with the given prefix
        def getWords(self, prefix: str) -> list[str]:
            tmp = self.root
            for c in prefix:
                if c not in tmp.children:
                    return []
                tmp = tmp.children[c]
            # dfs to find all children
            self.lst = []

        # find all words that are contained at the current head
        # localLst will be used to build the string
        def __dfs(self, head, localLst: list[str], prefix: str) -> None:
            if head.endOfWord:
                self.lst.append(prefix + ''.join(localLst.copy()))
                return
            for k in head.children.keys():
                localLst.append(k)
                self.__dfs(head.children[k], localLst, prefix)
                localLst.pop()

        def insert(self, word: str) -> None:
            tmp = self.root
            for c in word:
                # create trie node if one doesn't exist already
                if c not in tmp.children:
                    tmp.children[c] = TrieNode()
                tmp = tmp.children[c]
            tmp.endOfWord = True

    class TrieNode:
        def __init__(self):
            # string : TrieNode
            self.children = {}
            self.endOfWord = False

        # # print(products)
        # x = self.bin_search(products, 'mou')
        # # print(x)

    # only binary search for the answer if the prefix isn't in the trie already
    # store best 3 matching into trie

    # im gonna brute force instead since the trie-binary search way is taking me too long to code up

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()
        lst = []

        # loop thru each product (inner loop) based on
        # each possible prefix of our search word
        for i in range(1, len(searchWord)+1):
            tmp = []
            cnt = 0
            for p in products:
                if i <= len(p) and searchWord[:i] == p[:i]:
                    tmp.append(p)
                    cnt += 1
                if cnt == 3:
                    break
            print(tmp, searchWord[:i])
            lst.append(tmp)

        return lst




'''
online solution using binary search
# Binary Search
    products.sort()
    ans = []
    prefix = ''
    for ch in searchWord:
        prefix += ch
        l = bisect.bisect_left(products, prefix)
        r = bisect.bisect_right(products, prefix + '~')
        if l == r: # no such word
            break
        ans.append(products[ l : min(l+3, r) ])
    while len(ans) < len(searchWord): # append empty list when not found
        ans.append([])
    return ans
'''