


# even more optimized solution (no overwriting the index needed when inserting as we're adding words from right to left)
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        # set for debugging purposes and also skipping whats
        s = set()
        '''
        e.g. if word is 'ape', then the following strings will be inserted into the trie:
        e#ape, pe#ape, ape#ape, #ape
        '''
        for i in range(len(words)-1,-1,-1):
            word = words[i]
            if word in s: continue
            for j in range(len(word)+1):
                string = word[j:] + '#' + word
                self.trie.insert(i, string)
                # lst.append(string)
            s.add(word)
        # print(s)

    # prefix will be passed in like normal, but suffixes will be reversed
    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.getIndex(suffix + '#' + prefix)


class TrieNode:
    def __init__(self, i=None, end=False):
        self.index = i
        # <str,TrieNode>
        self.children = {}
        self.end = end
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, i:int, word:str) -> None:
        tmp = self.root
        for c in word:
            # create trie node if one doesn't exist already
            if c not in tmp.children:
                tmp.children[c] = TrieNode(i)
            # else:
            #     # overwrite the previous index
            #     tmp.children[c].index = i
            tmp = tmp.children[c]
        tmp.end = True

    # return the index of the string
    # returns -1 if not found
    def getIndex(self, string:str) -> int:
        tmp = self.root
        for c in string:
            if c not in tmp.children:
                return -1
            tmp = tmp.children[c]
        return tmp.index



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)










''' more optimized solution
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        # list for debugging purposes
        # lst = []

        # e.g. if word is 'ape', then the following strings will be inserted into the trie:
        # e#ape, pe#ape, ape#ape, #ape
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                string = word[j:] + '#' + word
                self.trie.insert(i, string)
                # lst.append(string)
        # print(lst)

    # prefix will be passed in like normal, but suffixes will be reversed
    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.getIndex(suffix + '#' + prefix)


class TrieNode:
    def __init__(self, i=None, end=False):
        self.index = i
        # <str,TrieNode>
        self.children = {}
        self.end = end
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, i:int, word:str) -> None:
        tmp = self.root
        for c in word:
            # create trie node if one doesn't exist already
            if c not in tmp.children:
                tmp.children[c] = TrieNode(i)
            else:
                # overwrite the previous index
                tmp.children[c].index = i
            tmp = tmp.children[c]
        tmp.end = True

    # return the index of the string
    # returns -1 if not found
    def getIndex(self, string:str) -> int:
        tmp = self.root
        for c in string:
            if c not in tmp.children:
                return -1
            tmp = tmp.children[c]
        return tmp.index



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
'''




# most optimized solution I've found online
'''
class WordFilter:

    def __init__(self, words: List[str]):
        self.pref = collections.defaultdict(set)
        self.suff = collections.defaultdict(set)
        seen = set()
        for i in range(len(words)-1, -1, -1):
            w = words[i]
            if w in seen:
                continue
            seen.add(w)
            for j in range(len(w)+1):
                self.pref[w[:j]].add(i)
                self.suff[w[j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.pref[prefix]
        b = self.suff[suffix]
        x = a & b
        return max(x) if x else -1
'''







# # brute force approach with a Trie
# class WordFilter:

#     def __init__(self, words: List[str]):
#         self.prefixTree = Trie()
#         # not actually a suffix tree but just named for argument's sake
#         self.suffixTree = Trie()
#         for i, word in enumerate(words):
#             self.prefixTree.insert(i, word)
#             self.suffixTree.insert(i, word[::-1])

#     # prefix will be passed in like normal, but suffixes will be reversed
#     def f(self, prefix: str, suffix: str) -> int:

#         set1 = self.prefixTree.getIndices(prefix)
#         set2 = self.suffixTree.getIndices(suffix[::-1])

#         # if either are empty, that means word with the given
#         # prefix and suffix does not exist
#         if not set1 or not set2:
#             return -1

#         return max(set1.intersection(set2))


# class TrieNode:
#     def __init__(self, i=-1, end=False):
#         self.s = set()
#         if i != -1:
#             self.s.add(i)
#         # <str,TrieNode>
#         self.children = {}
#         self.end = end


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, i: int, word: str) -> None:
#         tmp = self.root
#         for c in word:
#             # create trie node if one doesn't exist already
#             if c not in tmp.children:
#                 tmp.children[c] = TrieNode(i)
#             else:
#                 # record the index of the word
#                 tmp.children[c].s.add(i)
#             tmp = tmp.children[c]
#         tmp.end = True

#     # return a set of indices at which the prefix was found
#     # returns an empty set if prefix not found
#     def getIndices(self, prefix: str) -> set[int]:
#         tmp = self.root
#         for c in prefix:
#             if c not in tmp.children:
#                 return set()
#             tmp = tmp.children[c]
#         return tmp.s


# # Your WordFilter object will be instantiated and called as such:
# # obj = WordFilter(words)
# # param_1 = obj.f(prefix,suffix)
