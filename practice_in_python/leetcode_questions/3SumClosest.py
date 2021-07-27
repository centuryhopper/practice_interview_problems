

#region brute force O(n^3)
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        minSumDiff = float('inf')
        bestSum = None
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    curSum = (nums[i] + nums[j] + nums[k])
                    diff = abs(target - curSum)
                    # print(curSum, diff)
                    if diff < minSumDiff:
                        minSumDiff = diff
                        bestSum = curSum
                        # print(bestSum)
                    # we cannot achieve a difference better than this, so no point in searching any further
                    if diff == 0:
                        # print('here')
                        return bestSum
        return bestSum
#endregion



#region optimized O(n^2) time
class Solution:
    # two pointer approach O(n log n) time
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        bestSum = 0
        smallestDiff = float('inf')
        for i in range(n-2):
            j,k = i+1,n-1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                # if a perfect sum exists, then return it
                if curSum == target: return target
                # otherwise, move the pointers accordingly
                curDiff = abs(target - curSum)
                if curSum < target:
                    j+=1
                elif curSum > target:
                    k-=1
                if curDiff < smallestDiff:
                        smallestDiff = curDiff
                        bestSum = curSum
    
        return bestSum
#endregion