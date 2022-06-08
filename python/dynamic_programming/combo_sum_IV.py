class Solution:
    def rec(self,nums, target)->int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        cnt = 0
        for i in range(len(nums)):
            cnt += self.rec(nums, target-nums[i])
        return cnt
    def rec_memo(self,nums,target,memo)->int:
        if target == 0:
            return 1
        if target in memo:
            return memo[target]
        cnt = 0
        for i in range(len(nums)):
            if nums[i] <= target:
                cnt += self.rec_memo(nums, target-nums[i],memo)
        memo[target] = cnt
        return cnt


    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self.rec(nums, target)
        return self.rec_memo(nums,target,{})