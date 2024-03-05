class Solution:
    # high-level idea (unoptimized)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        seen = set()
        ans = []
        n, m = len(s), 10
        for i in range(n - m + 1):
            end = min(i + m, n)
            # print(s[i:end])
            if s[i:end] in seen:
                ans.append(s[i:end])
            else:
                seen.add(s[i:end])

        return set(ans)


# link: https://leetcode.com/problems/repeated-dna-sequences/description/
