

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # saves you from an O(n) runtime and space when input k is 1
        if (k == 1):
            return 0

        n = len(nums)

        m = {}
        cnt = 0
        for i in range(n):
            # puts value in map or updates it depending on its existence in the map
            m[nums[i]] = 1 if nums[i] not in m else m[nums[i]] + 1

            comp = k - nums[i]
            if comp in m:
                # checks for whether the comp and the current
                # number are equal
                if nums[i] == comp:
                    if m[comp] <= 1:
                        continue
                elif m[comp] <= 0:
                    continue

                cnt += 1
                m[comp] -= 1
                m[nums[i]] -= 1

        return cnt
