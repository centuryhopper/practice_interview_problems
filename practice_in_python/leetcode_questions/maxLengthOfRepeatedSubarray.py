



#region O(len(nums1) * len(nums2)) time and space solution
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0]*n for _ in range(m)]
        maxVal = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                    maxVal = max(maxVal, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return maxVal
#endregion