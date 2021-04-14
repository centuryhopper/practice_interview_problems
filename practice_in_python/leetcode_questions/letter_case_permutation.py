class Solution:
    def __init__(self):

        # O(1) lookup times for keeping track of when and when not to permute
        self.sett = set()

    # recursive backtracking solution
    def permute(self, s: list[str], l: int, r: int) -> None:

        # base case of finished processing
        # so add and print for debugging purposes
        if l > r:
            string = "".join(s)
            print(string)
            if string not in self.sett:
                self.sett.add(string)
            return

        for i in range(l, r+1):

            # recurse when current character is uppercase, but only do so
            # if we haven't seen such a permutation before
            s[i] = s[i].upper()
            string = "".join(s)
            if string not in self.sett:
                self.permute(s, l+1, r)

            # recurse when current character is lowercase, but only do so
            # if we haven't seen such a permutation before
            s[i] = s[i].lower()
            string = "".join(s)
            if string not in self.sett:
                self.permute(s, l+1, r)

    def letterCasePermutation(self, s: str) -> List[str]:

        self.permute(list(s), 0, len(s)-1)
        return list(self.sett)

    # iterative solution by https://www.youtube.com/watch?v=_Ipng-tBpSw&ab_channel=TimothyHChang
    # ret = [""]
    # for c in s:
    #     tmp = []
    #     if c.isalpha():
    #         for o in ret:
    #             tmp.append(o+c.lower())
    #             tmp.append(o+c.upper())
    #         print('letter:',ret)
    #     else:
    #         for o in ret:
    #             tmp.append(o+c)
    #         print('numeric:',ret)
    #     ret = tmp
    # return ret


#     def permute(self, s:list[str], l:int, r:int)->None:
#         if l > r:
#             print(s)
#             return
#         for i in range(l, r+1):
#             s[i], s[l] = s[l], s[i]
#             self.permute(s,l+1,r)

#             # unswap
#             s[i], s[l] = s[l], s[i]
