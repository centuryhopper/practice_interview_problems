from collections import defaultdict as defdic, deque
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # check if b is a subset of a
        # check if the count of all
        # unique letters in b are the same
        # as in those of a
        def is_sub(a:str, b:str, d) -> bool:
            if len(b) > len(a):
                return False
            for c in b:
                d[c] += 1
            for c in a:
                if c in d:
                    d[c] -= 1
            # less than or equal because count of any letter in a should be at least as many as
            # that same letter count in b
            return all(v <= 0 for _,v in d.items())

        def custom_join(B:list[str]) -> str:
            # records the overall best counts (i.e. max occurrance of each letter)
            d = defdic(int)
            # records current string's counts
            dhelper = defdic(int)
            lst = deque()
            for b in B:
                for c in b:
                    dhelper[c] += 1
                    tmp = d[c]
                    d[c] = max(d[c], dhelper[c])
                    # if there's a change, append the string (the difference) times
                    if d[c] > tmp:
                        for _ in range(d[c] - tmp):
                            lst.append(c)
                dhelper.clear()
            return ''.join(lst)

        # preprocess b's counts in a dict
        # then for every a in A, record its counts in the dict and compare

        # construct the final string from B:
        # print(custom_join(['ec', 'oc', 'ceo']))
        keyStr = custom_join(B)

        lst = []
        d = defdic(int)
        for a in A:
            if is_sub(a,keyStr,d):
                lst.append(a)
            d.clear()


        return lst