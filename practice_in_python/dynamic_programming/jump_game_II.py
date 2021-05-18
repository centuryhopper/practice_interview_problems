class Solution:
    '''
        Time: O(n^2) because we look ahead a distance of nums[i] for every nums[i]
        Space: O(n) because we always create a dp array the size of our input nums array to cache subproblems information
    '''
    # tabular approach
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        # 0 because it takes no steps to reach the last index if we're already there
        dp[n-1] = 0

        # work backwards and populate dp array
        # based on the smallest value you can reach
        # and add 1 to its dp value at that index
        for i in range(n-2,-1,-1):
            # not reachable if current pos is 0
            if nums[i] == 0:
                continue
            # offset reachable distance by the current position index
            reachableDist = (i+1)+nums[i]
            minVal = min(dp[i+1:reachableDist])
            # still cant reach
            if minVal == float('inf'):
                continue

            # find the smallest dp value from
            # the dp array and add 1
            dp[i] = minVal + 1
        # print(dp)
        return dp[0]

    #online solution https://www.youtube.com/watch?v=BRnRPLNGWIo&t=340s
    def jump_optimized(self, nums: list[int]) -> int:
        end, farthest, jump = 0,0,0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jump+=1
                end=farthest
        return jump

if __name__ == '__main__':
    print(Solution().jump([6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]))
