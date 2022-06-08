class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        O(n) time, O(1) space

        [1,2,1,3,2,5]

        6 => 0110
        lowestSetBit(6) = 2
        ans = [0,0]
        2&1 = 0 => [0^1,0]
        2&2 = 2 => [0^1,0^2]
        2&1 = 0 => [0^1^1,0^2]
        2&3 = 2 => [0^1^1,0^2^3]
        2&2 = 2 => [0^1^1,0^2^3^2]
        2&5 = 0 => [0^1^1^5,0^2^3^2]

        ans = [5,3]

        '''
        xor = functools.reduce(lambda x,y:x^y,nums)
        def getLowestOneBit(num:int)->int:
            multiple = 1
            while num & 1 != 1:
                num>>=1
                multiple*=2
            return multiple
        lowest = getLowestOneBit(xor)
        ans = [0,0]
        for num in nums:
            if lowest & num == 0:
                ans[0]^=num
            else:
                ans[1]^=num

        return ans