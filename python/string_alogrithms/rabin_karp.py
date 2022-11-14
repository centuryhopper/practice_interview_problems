import sys

'''
t = abcdabcda
p = cda
'''


# we can mod our hash function to avoid overflows in certain programming languages
PRIME = 101

# assume lowercase english letters
def rabinKarp(text, pat):
    n = len(text)
    m = len(pat)
    def makeHash(s: str) -> int:
        if not s.isalpha():
            return -1
        return sum((ord(c)-97) * (PRIME**(m-1-i)) for i,c in enumerate(s))
    def recomputeHash(s: str, oldIndex: int, newIndex: int, oldHash: int):
        newHash = oldHash - ((ord(s[oldIndex]) - 97) * PRIME**(m-1))
        newHash *= PRIME
        newHash += (ord(s[newIndex]) - 97)
        return newHash

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
        textHash = recomputeHash(text, i, min(i+m, n-1), textHash)

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



















