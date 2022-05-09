class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        def recMemo(piles, i, j, memo) -> int:
            # if there are two piles of stones left,
            # take the bigger pile
            if j-i == 1:
                return max(piles[i], piles[j])
            # avoid the same combos
            if (i, j) in memo:
                return memo[(i, j)]
            # take from the left
            choiceA = piles[i] + recMemo(piles, i+1, j, memo)
            # take from the right
            choiceB = piles[j] + recMemo(piles, i, j-1, memo)
            # cache the better choice
            memo[(i, j)] = max(choiceA, choiceB)
            # return the better choice
            return memo[(i, j)]
        return recMemo(piles, 0, len(piles)-1, {})
