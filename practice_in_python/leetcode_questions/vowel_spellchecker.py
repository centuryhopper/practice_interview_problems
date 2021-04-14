

class Solution:

    '''
    Input: wordlist = ["KiTe","kite","hare","Hare"],
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
    '''

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(s:str, vowels:set[str]) -> str:
            l = list(s)
            for i,c in enumerate(l):
                if c in vowels:
                    l[i] = '*'
            return ''.join(l)
        exactMatches = set()
        in_map = {}
        devoweled = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}
        lst = []
        # populate data structures
        for word in wordlist:
            # lowercase the word for consistency
            lower = word.lower()
            voweless = devowel(lower, vowels)
            exactMatches.add(word)
            # because there could be duplicates in the wordlist
            # we only want to store the first occurrance
            if lower not in in_map:
                in_map[lower] = word
            if voweless not in devoweled:
                devoweled[voweless] = word

        # finally, go thru every query string
        for qstr in queries:
            lower = qstr.lower()
            voweless = devowel(qstr.lower(), vowels)
            # find exact match
            if qstr in exactMatches:
                lst.append(qstr)
            # find case insensitive match
            elif lower in in_map:
                lst.append(in_map[lower])
            # find vowel errors
            elif voweless in devoweled:
                lst.append(devoweled[voweless])
            # append empty string in all other cases
            else:
                lst.append('')

        return lst









#online faster solution
# def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
#         set_wordlist = set(wordlist)

#         lc_wordlist = dict()
#         for w in wordlist:
#             lower = w.lower()
#             if lower in lc_wordlist:
#                 continue
#             lc_wordlist[lower] = w

#         vo_dict = dict()
#         for w, w_orig in lc_wordlist.items():
#             vowelless_w = w.lower().replace('a', '_').replace('e', '_').replace('i', '_').replace('o', '_').replace('u', '_')
#             if vowelless_w in vo_dict:
#                 continue

#             vo_dict[vowelless_w] = w_orig

#         ans = list()
#         for query in queries:
#             if query in set_wordlist:
#                 ans.append(query)
#             elif query.lower() in lc_wordlist:
#                 ans.append(lc_wordlist[query.lower()])
#             else:
#                 # Check for vowel errors
#                 vo_w = query.lower().replace('a', '_').replace('e', '_').replace('i', '_').replace('o', '_').replace('u', '_')
#                 if vo_w in vo_dict:
#                     ans.append(vo_dict[vo_w])
#                 else:
#                     # Nothing? return ""
#                     ans.append("")

#         return ans


















# failed attempt
# from collections import OrderedDict

# class Solution:

#     '''
#     Input: wordlist = ["KiTe","kite","hare","Hare"],
#     queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
#     '''

#     def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
#         # return
#         # st = OrderedDict((word, None) for word in wordlist)
#         st = wordlist
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         # print(st)
#         lst = []
#         for word in queries:
#             # case sensitive comparison
#             if word in st:
#                 # print(word)
#                 lst.append(word)
#             else:
#                 foundMatch = False
#                 for item in st:
#                     s1 = item.casefold()
#                     s2 = word.casefold()
#                     # print(s1)
#                     # print(s2)
#                     # print()
#                     # case insensitive comparison
#                     if s1 == s2:
#                         # print(item)
#                         lst.append(item)
#                         foundMatch = True
#                         break
#                     else:
#                         # check for vowel errors
#                         if len(s1) != len(s2): break
#                         # just for clarity, it really isn't logically needed
#                         # because we know it's aleady initialized to false
#                         foundMatch = False
#                         for i in range(len(s2)):
#                             # if they don't match
#                             # they better both be vowels or else
#                             # we will append an empty string
#                             if s2[i] != s1[i]:
#                                 if (s2[i] not in vowels or s1[i] not in vowels):
#                                     break;
#                             if i == len(s2) - 1: foundMatch = True
#                     # stop looking in the set for more
#                     # matches if we already found one
#                     if foundMatch:
#                         lst.append(item)
#                         break
#                 # append empty string
#                 # after iterating via
#                 # entire set and found no match
#                 if not foundMatch:
#                     lst.append('')

#         return lst





