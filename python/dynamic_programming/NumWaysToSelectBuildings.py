'''
There are only 2 valid patterns: ‘101’ and ‘010’. Think about how we can construct these 2 patterns from smaller patterns.

Count the number of subsequences of the form ‘01’ or ‘10’ first. Let n01[i] be the number of ‘01’ subsequences that exist in the prefix of s up to the ith building. How can you compute n01[i]?

Let n0[i] and n1[i] be the number of ‘0’s and ‘1’s that exists in the prefix of s up to i respectively. Then n01[i] = n01[i – 1] if s[i] == ‘0’, otherwise n01[i] = n01[i – 1] + n0[i – 1].

The same logic applies to building the n10 array and subsequently the n101 and n010 arrays for the number of ‘101’ and ‘010‘ subsequences.
'''


class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        # n+1 size for all of them because we account for the empty string to have 0 ways of selection
        n0 = [0]*(n+1)
        n1 = [0]*(n+1)
        n01 = [0]*(n+1)
        n10 = [0]*(n+1)
        n010 = [0]*(n+1)
        n101 = [0]*(n+1)
        for i in range(1,n+1):
            n0[i] = n0[i-1] + 1 if s[i-1] == '0' else n0[i-1]
        # print(n0)
        for i in range(1,n+1):
            n1[i] = n1[i-1] + 1 if s[i-1] == '1' else n1[i-1]
        # print(n1)
        for i in range(1,n+1):
            n01[i] = n01[i-1] + n0[i-1] if s[i-1] == '1' else n01[i-1]
        # print(n01)
        for i in range(1,n+1):
            n10[i] = n10[i-1] + n1[i-1] if s[i-1] == '0' else n10[i-1]
        # print(n10)
        for i in range(1,n+1):
            n010[i] = n010[i-1] + n01[i-1] if s[i-1] == '0' else n010[i-1]
        # print(n010)
        for i in range(1,n+1):
                n101[i] = n101[i-1] + n10[i-1] if s[i-1] == '1' else n101[i-1]
        # print(n101)

        return n010[-1] + n101[-1]
