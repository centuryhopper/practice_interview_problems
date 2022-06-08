

# my finalized solution
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        maxVal = 0
        curSum = 0
        i = 0
        for j,num in enumerate(nums):
            if num in s:
                # keep incrementing i until num is removed from the set
                # delete everything in between as well
                while num in s:
                    s.remove(nums[i])
                    curSum -= nums[i]
                    i += 1
            s.add(num)
            curSum += num
            maxVal = max(maxVal, curSum)
        return maxVal




'''
brute force
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i, j = 0, 1
        s = set()
        maxVal = nums[i]
        curSum = 0
        while j <= len(nums):

            if nums[j-1] in s:
                i+=1
                j = i+1
                s.clear()
                curSum = 0
                continue

            curSum += nums[j-1]
            s.add(nums[j-1])
            maxVal = max(maxVal, curSum)
            j+=1




        return maxVal
'''