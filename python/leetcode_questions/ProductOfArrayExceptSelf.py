
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # cheating way
        lstProd = 1
        lstProdWithoutZeros = 1
        cntZeros = 0
        for num in nums:
            lstProd *= num
            lstProdWithoutZeros *= num if num != 0 else 1
            cntZeros += 1 if num == 0 else 0
        if cntZeros == len(nums):
            return nums
        lst = []
        for num in nums:
            if num == 0:
                lst.append(lstProd if cntZeros > 1 else lstProdWithoutZeros)
            else:
                lst.append(lstProd//num)
        return lst
