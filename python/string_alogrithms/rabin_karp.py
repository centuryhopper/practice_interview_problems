import sys

'''
t = abcdabcda
p = cda
'''

PRIME = 101

# assume lowercase english letters
def rabinKarp(text, pat):
    def makeHash(s: str) -> int:
        if not s.isalpha():
            return -1
        return sum((ord(c)-97) * (PRIME**i) for i,c in enumerate(s))
    def recomputeHash(s: str, oldIndex: int, newIndex: int, oldHash: int, patternLen: str):
        newHash = oldHash - (ord(s[oldIndex]) - 97)
        newHash /= PRIME
        # print(f'{newIndex = }')
        newHash += (ord(s[newIndex]) - 97) * (PRIME ** (patternLen-1))
        return newHash

    n = len(text)
    m = len(pat)
    patHash = makeHash(pat)
    textHash = makeHash(text[:m])
    # print(patHash, textHash)
    ans = []
    for i in range(n-m+1):
        # curSnippet = text[i:i+m]
        # print(i,i+m,text[i:i+m], textHash)
        if patHash == textHash:
            # print('matching...')
            # print(text[i:i+m], pat)
            if text[i:i+m] == pat:
                # print(f'matched {pat}!')
                ans.append(i)
        # min call to avoid out of bounds
        textHash = recomputeHash(text, i, min(i+m, n-1), textHash, m)

    return ans

print(rabinKarp(sys.argv[1],sys.argv[2]))
# index = rabinKarp("TusharRoy", "sharRoy")
# print("Index ", index)
# index = rabinKarp("TusharRoy", "Roy")
# print("Index ", index)
# index = rabinKarp("TusharRoy", "shar")
# print("Index ", index)
# index = rabinKarp("TusharRoy", "usha")
# print("Index ", index)
# index = rabinKarp("TusharRoy", "Tus")
# print("Index ", index)
# index = rabinKarp("TusharRoy", "Roa")
# print("Index ", index)



















