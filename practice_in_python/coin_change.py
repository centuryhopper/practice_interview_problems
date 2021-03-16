# class Solution:

#     # greedy solution will not always work:
#     # for example coins: [1,4,5,10]   amount = 8
#     # greedy would be 5,1,1,1
#     # however, the optimal solution is 4,4

#     # assume all coins are positive integers
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         def rec_helper(coins, amount) -> int:
#             retVal = float('inf')
#             if amount < 0:
#                 return -1
#             if amount == 0:
#                 return 0
#             # reversed because greedy first
#             for coin in reversed(coins):
#                 # recurse with different amounts
#                 if coin <= amount:
#                     dfs = rec_helper(coins, amount-coin)
#                     if dfs == -1:
#                         return -1
#                     retVal = min(retVal, 1 + dfs)
#                     # print(retVal)

#             if retVal == float('inf'):
#                 # print('here')
#                 retVal = float('-inf')

#             return max(retVal, -1)

#         return rec_helper(coins, amount)


class Solution:

    def rec_helper(self, coins, amount) -> int:
        retVal = float('inf')
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        # reversed because greedy first
        for coin in reversed(coins):
            # recurse with different amounts
            if coin <= amount:
                dfs = self.rec_helper(coins, amount-coin)
                if dfs == -1: return -1
                retVal = min(retVal, 1 + dfs)
                # print(retVal)

        return retVal if retVal != float('inf') else -1


    def rec_helper_memo(self, coins, amount, memo) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        retVal = float('inf')
        # reversed because greedy first
        for coin in reversed(coins):
            # recurse with different amounts
            if coin <= amount:
                dfs = self.rec_helper_memo(coins, amount-coin, memo)
                # cannot go down a path that doesn't give you enough coins
                if dfs == -1:
                    continue
                retVal = min(retVal, 1 + dfs)
                # print(retVal)

        # if retVal is still +inf, then that means we couldn't take any coins, so return -1
        memo[amount] = retVal if retVal != float('inf') else -1

        return memo[amount]


    # greedy solution will not always work:
    # for example coins: [1,4,5,10]   amount = 8
    # greedy would be 5,1,1,1
    # however, the optimal solution is 4,4

    # assume all coins are positive integers
    def coinChange(self, coins: List[int], amount: int) -> int:

        # coins.sort()
        # print(coins)

        return self.rec_helper_memo(coins, amount, {})



