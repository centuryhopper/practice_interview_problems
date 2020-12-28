
class Solution:

    '''brute force recursive'''
    # start cur at position after the last character
    # and work backwards to the beginning of the string

    def helper_recursive(self, s: str, cur: int) -> int:

        # case when cur traverses right before the first character
        # bc of recursive calls with (cur - 2 passed in them)
        if cur == -1:
            return 1

        # if cur reaches first element
        if cur == 0:
            if s[cur] == '0':
                return 0
            return 1

        # handles case for decoding 10 and 20
        if (s[cur] == '0'):
            if s[cur - 1] == '2' or s[cur - 1] == '1':
                return self.helper_recursive(s, cur - 2)
            return 0

        res = 0

        # previous character is a 1 so we can definitely decode both
        # or if we have a number between 21 and 26, inclusive
        if s[cur - 1] == '1' or (s[cur - 1] == '2' and int(s[cur]) <= 6):
            res = self.helper_recursive(s, cur - 1) + self.helper(s, cur - 2)
        else:
            res = self.helper(s, cur - 1)

        return res

        # cache results
    def helper_memo(self, s: str, cur: int, memo: dict[int, int]) -> int:

        # if we've already cached this result in another recursive call,
        # then just return it instead of recomputing it
        if cur in memo:
            return memo[cur]

        # case when cur traverses right before the first character
        # bc of recursive calls with (cur - 2 passed in them)
        if cur == -1:
            memo[cur] = 1
            return 1

        # if cur reaches first element
        if cur == 0:
            if s[cur] == '0':
                memo[cur] = 0
                return 0
            memo[cur] = 1
            return 1

        # handles case for decoding 10 and 20
        if s[cur] == '0':
            if s[cur - 1] == '2' or s[cur - 1] == '1':
                memo[cur] = self.helper_memo(s, cur - 2, memo)
                return memo[cur]
            memo[cur] = 0
            return 0

        # previous character is a 1 so we can definitely decode both
        # or if we have a number between 21 and 26, inclusive
        if s[cur - 1] == '1' or (s[cur - 1] == '2' and int(s[cur]) <= 6):
            memo[cur] = self.helper_memo(
                s, cur - 1, memo) + self.helper_memo(s, cur - 2, memo)
        else:
            memo[cur] = self.helper_memo(s, cur - 1, memo)

        return memo[cur]

    def helper_dp(self, s, dp: list[int]) -> int:
        if s[0] == '0': return 0

        # empty string and first character case, respectively
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s)):
            prevChar = s[i - 1]
            prevPrevChar = s[i - 2]

            # accept the i - 2 answer if we have a 20 or 10
            if prevChar == '0':
                if prevPrevChar == '2' or prevPrevChar == '1':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                # accept 1x where x is any single-digit number or accept a 2x, where 0 <= x <= 6
                # either way, we accept i - 1 and i - 2
                if prevPrevChar == '1' or (prevPrevChar == '2' and prevChar <= 6):
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]

        # bottom up'd to the string length index
        return dp[len(s)]


    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0:
            return 1
        # return self.helper_recursive(s, len(s) - 1)

        # memo = {}
        # return self.helper_memo(s, len(s) - 1, memo)

        dp = [-1 for i in range(len(s) + 1)]
        return self.helper_dp(s, dp)



# print([-1 for i in range(len('123') + 1)])