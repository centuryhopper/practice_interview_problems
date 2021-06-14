

# my solutions
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        def rec(stones, curSum, aliceTurn, i, j, aSum, bSum) -> int:
            # game is over
            if i > j:
                return aSum - bSum
            # alice turn (maximize the difference)
            if aliceTurn:
                choice1 = rec(
                    stones, curSum-stones[i], False, i+1, j, aSum+curSum-stones[i], bSum)
                choice2 = rec(
                    stones, curSum-stones[j], False, i, j-1, aSum+curSum-stones[j], bSum)
                return max(choice1, choice2)
            # bob's turn (minimize the difference)
            choice1 = rec(stones, curSum -
                          stones[i], True, i+1, j, aSum, bSum+curSum-stones[i])
            choice2 = rec(stones, curSum -
                          stones[j], True, i, j-1, aSum, bSum+curSum-stones[j])
            return min(choice1, choice2)

        def recMemo(stones, curSum, i, j, memo) -> int:
            # there's only one element in the array
            # so no one can gain any points
            # don't really need this check because every array will be at least size 2
            if i == j:
                return 0
            # there are two elements left in the array
            # so take which ever one is bigger
            if j - i == 1:
                return max(stones[i], stones[j])
            # avoid repeated computation if possible
            if (i, j) in memo:
                return memo[(i, j)]

            choice1 = curSum - \
                stones[i] - recMemo(stones, curSum-stones[i], i+1, j, memo)
            choice2 = curSum - \
                stones[j] - recMemo(stones, curSum-stones[j], i, j-1, memo)
            memo[(i, j)] = max(choice1, choice2)
            return memo[(i, j)]
        return recMemo(stones, sum(stones), 0, len(stones)-1, {})


# online solution (dp w/o recursion)
# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         n = len(stones)
#         dp = [0] * n

#         for i in range(n - 1, -1, -1):
#             v = stones[i]
#             run_sum = 0

#             for j in range(i + 1, n):
#                 new_run = run_sum+stones[j]
#                 dp[j] = max(new_run - dp[j], run_sum+v - dp[j - 1])
#                 run_sum = new_run
#         return dp[n - 1]
