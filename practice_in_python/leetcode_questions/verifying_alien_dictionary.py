# from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        d = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            if words[i] == words[i+1]: continue
            a,b = len(words[i]), len(words[i+1])


            try:
                if a > b:
                    if words[i].index(words[i+1]) == 0:
                        return False
                if b > a:
                    if words[i+1].index(words[i]) == 0:
                        continue
            except:
                pass

            # if at least one character comparison on the same
            # index is lexicographically greater than continue
            passed = True
            for j in range(min(a,b)):
                first = d[words[i][j]]
                second = d[words[i+1][j]]
                print(first, second)
                if first == second:
                    continue
                if first > second:
                    passed = False
                    break
                if first < second:
                    passed = True
                    break

            if not passed:
                print(words[i][j], words[i+1][j])
                return False

            # check for prefix
            # if a > b



        return True