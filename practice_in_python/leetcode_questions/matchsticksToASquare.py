
# region my final solution
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # need at least 4 for a square
        if len(matchsticks) < 4: return False

        # get max number in matchsticks since the least possible number will involve it
        # each side of square should be of sum(matchsticks) // 4
        summ = sum(matchsticks)
        if summ % 4 != 0: return False
        targetLen = summ // 4

        # sorting the array in decreasing order because this
        # will decrease recursion time
        matchsticks.sort(reverse=True)

        def rec(m, a, b, c, d, i) -> bool:
            nonlocal targetLen
            # make sure all matchsticks have been used before checking
            if i == len(m):
                return a == b == c == d == targetLen
            for j in range(4):
                # try out a,b,c,and d
                if j == 0:
                    if a + m[i] <= targetLen:
                        if rec(m, a+m[i], b, c, d, i+1):
                            return True
                if j == 1:
                    if b + m[i] <= targetLen:
                        if rec(m, a, b+m[i], c, d, i+1):
                            return True
                if j == 2:
                    if c + m[i] <= targetLen:
                        if rec(m, a, b, c+m[i], d, i+1):
                            return True
                if j == 3:
                    if d + m[i] <= targetLen:
                        if rec(m, a, b, c, d+m[i], i+1):
                            return True
            return False
        return rec(matchsticks, 0, 0, 0, 0, 0)

# endregion


#region unbelievable bitmask w/memoization solution provided by leetcode
def makesquare(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # If there are no matchsticks, then we can't form any square.
    if not nums:
        return False

    # Number of matchsticks
    L = len(nums)

    # Possible perimeter of our square
    perimeter = sum(nums)

    # Possible side of our square from the given matchsticks
    possible_side =  perimeter // 4

    # If the perimeter isn't equally divisible among 4 sides, return False.
    if possible_side * 4 != perimeter:
        return False

    # Memoization cache for the dynamic programming solution.
    memo = {}

    #region helper method
    # mask and the sides_done define the state of our recursion.
    def recurse(mask, sides_done):
        nonlocal memo

        # This will calculate the total sum of matchsticks used till now using the bits of the mask.
        total = 0
        for i in range(L - 1, -1, -1):
            if not (mask & (1 << i)):
                total += nums[L - 1 - i]

        # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
        if total > 0 and total % possible_side == 0:
            sides_done += 1

        # If we were successfully able to form 3 sides, return True
        if sides_done == 3:
            return True

        # If this recursion state has already been calculated, just return the stored value.
        if (mask, sides_done) in memo:
            return memo[(mask, sides_done)]

        # Common variable to store answer from all possible further recursions from this step.
        ans = False

        # rem stores available space in the current side (incomplete).
        c = int(total / possible_side)
        rem = possible_side * (c + 1) - total

        # Iterate over all the matchsticks
        for i in range(L - 1, -1, -1):

            # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
            if nums[L - 1 - i] <= rem and mask&(1 << i):

                # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                if recurse(mask ^ (1 << i), sides_done):
                    ans = True
                    break
        # cache the result for the current recursion state.
        memo[(mask, sides_done)] = ans
        return ans
    #endregion

    # recurse with the initial mask with all matchsticks available.
    # e.g. 15 => 111111111111111
    # 0 means used, 1 means available
    return recurse((1 << L) - 1, 0)
'''
Complexity Analysis

Time Complexity : O(N \times 2^N)O(N×2
N
 ). At max 2^N2
N
  unique bit masks are possible and during every recursive call, we iterate our original matchsticks array to sum up the values of matchsticks used to update the sides_formed variable.

Space Complexity : O(N + 2^N)O(N+2
N
 ) because NN is the stack space taken up by recursion and 4 \times 2^N4×2
N
  = O(2^N)O(2
N
 ) is the max possible size of our cache for memoization.

The size of the cache is defined by the two variables sides_formed and mask. The number of different values that sides_formed can take = 4 and number of unique values of mask = 2^N2
N
 .
'''
#endregion

# region working solution that's cleaner than mine
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # need at least 4 for a square
        if len(matchsticks) < 4:
            return False

        # get max number in matchsticks since the least possible number will involve it
        # each side of square should be of sum(matchsticks) // 4
        summ = sum(matchsticks)
        if summ % 4 != 0:
            return False
        targetLen = summ // 4
        sides = [0]*4

        # sorting the array in decreasing order because this
        # will decrease recursion time
        matchsticks.sort(reverse=True)

        def rec(m, sides, i) -> bool:
            nonlocal targetLen
            # make sure all matchsticks have been used before checking
            if i == len(m):
                return sides[0] == sides[1] == sides[2] == sides[3] == targetLen
            for j in range(4):
                if sides[j] + m[i] <= targetLen:
                    sides[j] += m[i]
                    if rec(m, sides, i+1):
                        return True
                    # undo state change
                    sides[j] -= m[i]
            return False

        return rec(matchsticks, sides, 0)


# endregion

# region brute force (super slow)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # get max number in matchsticks since the least possible number will involve it
        # each side of square should be of sum(matchsticks) // 4
        targetLen = sum(matchsticks) // 4
        cnt = 0

        def rec(matchsticks, a, b, c, d) -> bool:
            nonlocal targetLen, cnt
            cnt += 1
            if a == b == c == d and a == targetLen:
                # print(a,b,c,d)
                # print(cnt)
                return True
            ret = False
            for i, m in enumerate(matchsticks):
                # already in our path
                if m == None:
                    continue
                matchsticks[i] = None
                if a + m <= targetLen:
                    ret |= rec(matchsticks, a+m, b, c, d)
                elif b + m <= targetLen:
                    ret |= rec(matchsticks, a, b+m, c, d)
                elif c + m <= targetLen:
                    ret |= rec(matchsticks, a, b, c+m, d)
                elif d + m <= targetLen:
                    ret |= rec(matchsticks, a, b, c, d+m)
                matchsticks[i] = m
            # print(cnt)
            # no path found that makes a square
            return ret

        return rec(matchsticks, 0, 0, 0, 0)
# endregion
