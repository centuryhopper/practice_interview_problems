class Solution:
    def maxLength(self, ss: list[str]) -> int:
        def hasDupes(s) -> bool:
            mask = 0
            for c in s:
                # already seen, so return True
                if mask & (1 << (ord(c) - 97)):
                    return True
                mask |= 1 << (ord(c) - 97)
            return False

        ans = ['']
        for s in ss:
            for elem in ans:
                if hasDupes(s+elem):
                    continue
                ans.append(s+elem)

        return len(max(ans, key=lambda x: len(x)))
